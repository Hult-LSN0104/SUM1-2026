# photogram.py - Starter
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

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
    
    # TODO BONUS: Implement a Comment model and relationship
    
    def __repr__(self):
        return f'<Post {self.id}>'

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
    # TODO: Get all posts from database, ordered by newest first
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # TODO: Get specific post by ID
    return render_template('post_detail.html')

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # TODO: 
        # 1. Validate and save the uploaded image
        # 2. Get the caption from the form
        # 3. Create a new post in the database
        # 4. Handle errors (invalid file type, no file uploaded, etc.)
        return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    # TODO: Increment the like count for a post
    return redirect(url_for('index'))

# TODO BONUS: Add routes for commenting on posts

if __name__ == '__main__':
    app.run(debug=True)