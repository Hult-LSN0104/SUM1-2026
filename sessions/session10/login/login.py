"""
Simple Flask Login & Database Example
Run: python login.py
Then visit: http://localhost:5000
"""

from flask import Flask, request, session, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = "your_secret_key_change_this"

db = SQLAlchemy(app)

# ============================================================================
# DATABASE MODEL
# ============================================================================

class User(db.Model):
    """Defines what a User looks like in the database"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

# Create database tables
with app.app_context():
    db.create_all()
    print("✅ Database ready!")

# ============================================================================
# HTML TEMPLATES
# ============================================================================

BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        form { max-width: 300px; }
        input { display: block; margin: 10px 0; padding: 8px; width: 100%; }
        button { padding: 10px 20px; background: #0099ff; color: white; border: none; cursor: pointer; }
        .message { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    {{ content | safe }}
</body>
</html>
"""

# ============================================================================
# ROUTES
# ============================================================================

@app.route("/")
def home():
    """Home page - shows login/signup or welcome message"""
    if "username" in session:
        return render_template_string(BASE_TEMPLATE, title="Home", content=f"""
            <h1>Welcome, {session['username']}! 👋</h1>
            <p>You are logged in.</p>
            <a href="/dashboard"><button>Go to Dashboard</button></a>
            <a href="/logout"><button style="background: #ff6b6b;">Log Out</button></a>
        """)
    
    return render_template_string(BASE_TEMPLATE, title="Home", content="""
        <h1>Welcome to the App</h1>
        <p>Please log in or create an account.</p>
        <a href="/register"><button>Sign Up</button></a>
        <a href="/login"><button>Log In</button></a>
    """)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Sign up for a new account"""
    message = ""
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Validation
        if not username or not password:
            message = '<div class="message error">❌ Username and password required!</div>'
        elif len(password) < 3:
            message = '<div class="message error">❌ Password must be at least 3 characters!</div>'
        elif User.query.filter_by(username=username).first():
            message = '<div class="message error">❌ Username already taken!</div>'
        else:
            # Create new user
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            message = '<div class="message success">✅ Account created! <a href="/login">Log in here</a></div>'
    
    return render_template_string(BASE_TEMPLATE, title="Sign Up", content=f"""
        <h2>Create Account</h2>
        {message}
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign Up</button>
        </form>
        <p>Already have an account? <a href="/login">Log in</a></p>
    """)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in to your account"""
    message = ""
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Find user in database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
        if user and user.password == password:
            # Store in session (user is now logged in)
            session["user_id"] = user.id
            session["username"] = user.username
            message = f'<div class="message success">✅ Welcome, {username}! Redirecting...</div>'
            # In a real app, you'd redirect here
            return render_template_string(BASE_TEMPLATE, title="Login", content=f"""
                {message}
                <p><a href="/dashboard">Click here if not redirected</a></p>
                <script>setTimeout(() => window.location.href = '/dashboard', 1000)</script>
            """)
        else:
            message = '<div class="message error">❌ Invalid username or password!</div>'
    
    return render_template_string(BASE_TEMPLATE, title="Log In", content=f"""
        <h2>Log In</h2>
        {message}
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
        <p>Don't have an account? <a href="/register">Sign up</a></p>
    """)

@app.route("/dashboard")
def dashboard():
    """Protected page - only for logged-in users"""
    if "user_id" not in session:
        return render_template_string(BASE_TEMPLATE, title="Dashboard", content="""
            <div class="message error">❌ You must be logged in to view this page!</div>
            <a href="/login"><button>Log In</button></a>
        """)
    
    # Get user info from database
    user = User.query.get(session["user_id"])
    
    return render_template_string(BASE_TEMPLATE, title="Dashboard", content=f"""
        <h1>Dashboard 📊</h1>
        <p>Hello, <strong>{session['username']}</strong>!</p>
        <p>This page is only visible to logged-in users.</p>
        <hr>
        <p><strong>Your Account Info:</strong></p>
        <p>Username: {user.username}</p>
        <p>User ID: {user.id}</p>
        <hr>
        <a href="/logout"><button style="background: #ff6b6b;">Log Out</button></a>
    """)

@app.route("/logout")
def logout():
    """Log out and clear session"""
    username = session.get("username", "User")
    session.clear()
    
    return render_template_string(BASE_TEMPLATE, title="Logged Out", content=f"""
        <div class="message success">✅ Goodbye, {username}! You've been logged out.</div>
        <a href="/login"><button>Log In Again</button></a>
        <a href="/register"><button>Create New Account</button></a>
    """)

@app.route("/users")
def view_users():
    """Admin view - see all users in database (for learning only!)"""
    users = User.query.all()
    
    user_list = "<ul>"
    for user in users:
        user_list += f"<li>{user.username} (ID: {user.id})</li>"
    user_list += "</ul>"
    
    return render_template_string(BASE_TEMPLATE, title="All Users", content=f"""
        <h2>All Users in Database</h2>
        <p>Total users: {len(users)}</p>
        {user_list if users else "<p>No users yet</p>"}
        <a href="/"><button>Back Home</button></a>
    """)

# ============================================================================
# RUN THE APP
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Flask Login App Starting!")
    print("=" * 50)
    print("Visit: http://localhost:5000")
    print("Admin: http://localhost:5000/users")
    print("=" * 50)
    app.run(debug=True)