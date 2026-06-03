# Import libraries
import random # → for random.choices()
import string # → for string.ascii_letters and string.digits
import hashlib # hashlib → for hashlib.sha256()

# Get a password from a user
pwd = input("Password: ")

# Generate a salt of random length between 5 and 20 characters, consisting of letters and digits
salt_length = random.randint(5, 20)

# Join the randomly generated characters to create the salt
salt = ''.join(random.choices(string.ascii_letters + string.digits, k=salt_length)) 

# Hash the password using SHA-256 using the hashlib library, and encode the password before hashing
hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()

# Combine the salt and the hashed password
salt_and_hashed_pwd = salt + hashed_pwd

# Print each out: 
print("Salt:", salt)
print("Hashed Password:", hashed_pwd)
print("Salt + Hashed Password:", salt_and_hashed_pwd)   