# Flask Login & Database Guide for Beginners

## What You Need

```bash
pip install flask flask-sqlalchemy
```

---

## The Big Picture

```
User signs up → Store in Database
User logs in → Check Database
User stays logged in → Use Session
```

---

## Part 1: Set Up the Database

In Flask, a **database model** defines what data you store. Here's a User:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define what a User looks like in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'
```

**What this means:**
- `id` — Unique number for each user (1, 2, 3...)
- `username` — The login name (e.g., "alice")
- `password` — The password (e.g., "secret123")
- `unique=True` — No two users can have the same username
- `nullable=False` — These fields can't be empty

---

## Part 2: Create the Database

```python
# Run this ONCE to create the database
with app.app_context():
    db.create_all()
    print("Database created!")
```

This creates a file called `users.db` that stores your users.

---

## Part 3: Register (Sign Up)

```python
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already taken!"
        
        # Create new user and save to database
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return "✅ Account created! <a href='/login'>Log in here</a>"
    
    # Show registration form
    return """
    <form method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Sign Up</button>
    </form>
    """
```

---

## Part 4: Login

```python
from flask import session

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Find user in database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
        if user and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.username
            return f"✅ Welcome, {username}! <a href='/dashboard'>Go to dashboard</a>"
        else:
            return "❌ Invalid username or password"
    
    # Show login form
    return """
    <form method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Log In</button>
    </form>
    """
```

---

## Part 5: Protected Page (Logged In Users Only)

```python
@app.route("/dashboard")
def dashboard():
    # Check if user is logged in
    if "user_id" not in session:
        return "❌ You're not logged in! <a href='/login'>Log in</a>"
    
    username = session["username"]
    return f"""
    <h1>Welcome, {username}!</h1>
    <p>This page is only for logged-in users.</p>
    <a href='/logout'>Log Out</a>
    """
```

---

## Part 6: Logout

```python
@app.route("/logout")
def logout():
    session.clear()
    return "✅ You've been logged out! <a href='/login'>Log in again</a>"
```

---

## Complete Example App

Here's everything together:

```python
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = "your_secret_key_here"  # Required for sessions
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create database
with app.app_context():
    db.create_all()

# Home page
@app.route("/")
def home():
    if "username" in session:
        return f"Welcome back, {session['username']}! <a href='/dashboard'>Dashboard</a> | <a href='/logout'>Logout</a>"
    return "<a href='/register'>Sign Up</a> | <a href='/login'>Log In</a>"

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if User.query.filter_by(username=username).first():
            return "❌ Username taken!"
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return "✅ Account created! <a href='/login'>Log in</a>"
    
    return """
    <h2>Sign Up</h2>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button>Sign Up</button>
    </form>
    """

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.username
            return f"✅ Welcome, {username}! <a href='/dashboard'>Dashboard</a>"
        
        return "❌ Invalid login!"
    
    return """
    <h2>Log In</h2>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button>Log In</button>
    </form>
    """

# Protected page
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return "❌ Log in first! <a href='/login'>Log in</a>"
    
    return f"""
    <h1>Dashboard</h1>
    <p>Hello, {session['username']}!</p>
    <a href='/logout'>Log Out</a>
    """

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return "✅ Logged out! <a href='/login'>Log in again</a>"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## How It Works (Step by Step)

**User signs up:**
1. User enters username & password on `/register`
2. Flask checks if username already exists in database
3. If not, Flask creates a new `User` object
4. `db.session.add()` and `db.session.commit()` save it to the database ✅

**User logs in:**
1. User enters username & password on `/login`
2. Flask searches database: `User.query.filter_by(username=username).first()`
3. If found and password matches, Flask stores their ID in `session`
4. User can now access protected pages ✅

**Protected pages:**
1. Check if `"user_id"` is in the `session`
2. If yes, show the page
3. If no, send them to login ✅

---

## Key Concepts

| Concept | What It Does |
|---|---|
| `db.Model` | Defines the structure of your database table |
| `db.session.add()` | Add a new record to database |
| `db.session.commit()` | Save changes to database |
| `User.query.filter_by()` | Search the database |
| `session` | Store user info (logged in or not) |

---

## Security Notes (For Students)

⚠️ **This is simplified for learning!** In production:

```python
# ❌ DON'T store passwords as plain text!
# ✅ DO use password hashing:

from werkzeug.security import generate_password_hash, check_password_hash

# When registering:
hashed = generate_password_hash(password)
new_user = User(username=username, password=hashed)

# When logging in:
if user and check_password_hash(user.password, password):
    # Password is correct!
```

---

## Testing the App

```bash
python app.py
```

1. Visit `http://localhost:5000/register`
2. Create an account: username=`alice`, password=`secret`
3. Visit `http://localhost:5000/login`
4. Log in with alice/secret
5. Visit `http://localhost:5000/dashboard` (protected!)
6. Log out with `/logout`

---

## Common Student Questions

**Q: Where is the database stored?**
A: In a file called `users.db` in your project folder.

**Q: Can I see what's in the database?**
A: Yes! Download "DB Browser for SQLite" to open and view `users.db`.

**Q: Why use `session` instead of just checking the database every time?**
A: Sessions are faster and don't require a database lookup on every page.

**Q: Why is `app.secret_key` required?**
A: Flask encrypts the session data. Without a secret key, it won't work.