# Flask Login & Database Visual Guide

## What's Happening (Behind the Scenes)

```
USER VISITS APP
       ↓
   Register?  ↔  Store in Database
       ↓
   Login?     ↔  Check Database
       ↓
   Stay Logged In?  ↔  Use Session (Cookie)
```

---

## The Database Table

Think of the database like a spreadsheet with users:

```
┌─────────────────────────────────────────┐
│              USERS TABLE                │
├─────┬──────────────┬──────────────────┤
│ ID  │   USERNAME   │    PASSWORD      │
├─────┼──────────────┼──────────────────┤
│  1  │    alice     │    secret123     │
├─────┼──────────────┼──────────────────┤
│  2  │     bob      │    pass456       │
├─────┼──────────────┼──────────────────┤
│  3  │   charlie    │    mypassword    │
└─────┴──────────────┴──────────────────┘
```

In Python code:
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)      # 1, 2, 3...
    username = db.Column(db.String(80))               # alice, bob...
    password = db.Column(db.String(120))              # secret123...
```

---

## Sign Up Flow

```
User fills form:
  Username: alice
  Password: secret123
       ↓
Flask gets form data
  username = "alice"
  password = "secret123"
       ↓
Check: Does alice already exist?
  User.query.filter_by(username="alice").first()
       ↓
   NO → Create new user object
       ↓
   Save to database
  db.session.add(new_user)
  db.session.commit()
       ↓
   ✅ Success! "Account created"
```

---

## Login Flow

```
User fills form:
  Username: alice
  Password: secret123
       ↓
Flask gets form data
  username = "alice"
  password = "secret123"
       ↓
Search database for alice
  user = User.query.filter_by(username="alice").first()
       ↓
Check password matches
  if user and user.password == "secret123":
       ↓
   YES → Create session (cookies)
  session["user_id"] = 1
  session["username"] = "alice"
       ↓
   ✅ User is now logged in!
```

---

## Session (Cookies)

When a user logs in, Flask stores data in a **session cookie**:

```
Browser stores:
┌─────────────────────────────────┐
│     session cookie              │
├─────────────────────────────────┤
│ user_id: 1                      │
│ username: alice                 │
│ (encrypted by Flask)            │
└─────────────────────────────────┘

Every time they visit, Flask checks:
  if "user_id" in session:
      # User is logged in!
  else:
      # User is NOT logged in
```

---

## Protected Page Flow

```
User visits /dashboard
       ↓
Flask checks session:
  if "user_id" not in session:
       ↓
  YES → "❌ Log in first!"
  NO  → Show dashboard
       ↓
  ✅ Welcome, alice!
```

---

## Database Queries (Cheat Sheet)

```python
# ADD a new user
new_user = User(username="alice", password="secret123")
db.session.add(new_user)
db.session.commit()

# FIND a user by username
user = User.query.filter_by(username="alice").first()
# Returns: <User alice> or None

# GET a user by ID
user = User.query.get(1)
# Returns: <User alice> or None

# GET all users
users = User.query.all()
# Returns: [<User alice>, <User bob>, <User charlie>]

# COUNT users
count = User.query.count()
# Returns: 3

# DELETE a user
user = User.query.get(1)
db.session.delete(user)
db.session.commit()

# UPDATE a user
user = User.query.get(1)
user.password = "newpassword"
db.session.commit()
```

---

## Life of a Login Session

```
Step 1: User signs up
┌──────────────────────────────────┐
│  User table in database          │
├──────────────────────────────────┤
│ username: alice                  │
│ password: secret123              │
└──────────────────────────────────┘

Step 2: User logs in
┌──────────────────────────────────┐
│  Browser session cookie          │
├──────────────────────────────────┤
│ user_id: 1                       │
│ username: alice                  │
└──────────────────────────────────┘

Step 3: User visits any page
Flask checks: "Is alice's ID in the cookie?"
  → YES → Show page
  → NO  → Send to login

Step 4: User logs out
Flask clears the cookie:
session.clear()
  → Cookie deleted
  → User is no longer logged in
  → Next page requires login again
```

---

## Common Database Operations

### Creating a User
```python
new_user = User(username="alice", password="secret")
db.session.add(new_user)
db.session.commit()
# ✅ alice is now in the database
```

### Finding a User
```python
user = User.query.filter_by(username="alice").first()
if user:
    print(f"Found: {user.username}")
else:
    print("User not found")
```

### Checking Password
```python
user = User.query.filter_by(username="alice").first()
if user.password == "secret":
    # Password is correct!
else:
    # Wrong password
```

### Logging In
```python
session["user_id"] = user.id
session["username"] = user.username
# Now they're logged in
```

### Checking If Logged In
```python
if "user_id" in session:
    # User is logged in
else:
    # User is NOT logged in
```

### Logging Out
```python
session.clear()
# User is now logged out
```

---

## File Structure

```
my_app/
│
├── flask_login_app.py          ← Your Flask app code
│
├── users.db                    ← Database file (created automatically)
│
└── templates/
    └── (optional HTML files)
```

---

## To Run It

```bash
# Install dependencies
pip install flask flask-sqlalchemy

# Run the app
python flask_login_app.py

# Visit in browser
http://localhost:5000
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: flask_sqlalchemy` | Run `pip install flask-sqlalchemy` |
| `RuntimeError: Working outside of application context` | Make sure code is inside `with app.app_context():` |
| `IntegrityError: UNIQUE constraint failed` | Username already exists. Try a different username |
| Session not working | Check that `app.secret_key = "something"` is set |
| Database errors | Delete `users.db` and restart the app |

---

## Next Steps (Advanced)

These are beyond the scope but good to know:

- **Password hashing:** Don't store plain passwords! Use `werkzeug.security`
- **Email verification:** Send verification email on signup
- **"Remember me":** Keep users logged in longer
- **Profile pictures:** Store images with users
- **Relationships:** Users have posts, comments, etc.
- **Permissions:** Admin users, roles, etc.