from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import uuid
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photogram.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-key-change-in-production'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Make sure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer, default=0)
    
    # Relationship with Comment model (one-to-many)
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Post {self.id}>'
        
    def time_since(self):
        """Returns a human-readable time string like '2 hours ago'"""
        delta = datetime.utcnow() - self.created_at
        
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        else:
            return "just now"

# Comment Model 
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    username = db.Column(db.String(30), default="user")  # Simplified - real app would link to user model

    def __repr__(self):
        return f'<Comment {self.id}>'
        
    def time_since(self):
        """Returns a human-readable time string like '2 hours ago'"""
        delta = datetime.utcnow() - self.created_at
        
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        else:
            return "just now"



# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Check if image file exists in the request
        if 'image' not in request.files:
            flash('No image file selected', 'danger')
            return redirect(request.url)
            
        file = request.files['image']
        
        # Check if user submitted an empty form (browser submits empty file without filename)
        if file.filename == '':
            flash('No image file selected', 'danger')
            return redirect(request.url)
            
        # Process file if it exists and has allowed extension
        if file and allowed_file(file.filename):
            # Create unique filename to avoid collisions
            filename = secure_filename(file.filename)
            file_ext = os.path.splitext(filename)[1]
            unique_filename = f"{uuid.uuid4().hex}{file_ext}"
            
            # Save the file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)
            
            # Get caption from form
            caption = request.form.get('caption', '')
            
            # Create new post
            new_post = Post(
                image_filename=unique_filename,
                caption=caption
            )
            
            db.session.add(new_post)
            db.session.commit()
            
            flash('Your post has been created!', 'success')
            return redirect(url_for('post_detail', post_id=new_post.id))
        else:
            flash('Invalid file type. Allowed types: png, jpg, jpeg, gif', 'danger')
            return redirect(request.url)
            
    return render_template('create.html')

@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    
    # Redirect back to referring page (either index or post_detail)
    next_page = request.referrer
    if not next_page:
        next_page = url_for('index')
    return redirect(next_page)

# BONUS: Routes for commenting
@app.route('/comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment_content = request.form.get('content', '')
    
    if comment_content.strip():
        comment = Comment(
            content=comment_content,
            post_id=post.id,
            username="user"  # Simplified - real app would use logged-in user
        )
        db.session.add(comment)
        db.session.commit()
    
    # Redirect back to post detail
    return redirect(url_for('post_detail', post_id=post_id))

@app.template_filter('file_url')
def file_url(filename):
    """Template filter to generate URL for uploaded files"""
    return url_for('static', filename=f'uploads/{filename}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)