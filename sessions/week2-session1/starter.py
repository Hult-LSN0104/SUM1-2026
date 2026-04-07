# =============================================================================
# LSN-0104 | Week 2, Session 3
# Working with Strings
# =============================================================================
#
# Strings are everywhere in business data — customer names, email addresses,
# product codes, addresses. Real-world data is almost always messy:
# extra spaces, inconsistent capitalisation, typos in formatting.
#
# Useful string methods for today:
#   .strip()        removes leading and trailing whitespace
#   .lower()        converts to lowercase
#   .upper()        converts to UPPERCASE
#   .title()        Capitalises Every Word
#   .replace(a, b)  replaces all occurrences of a with b
#   .split(x)       splits a string into a list at every x
#   .startswith(x)  returns True if the string starts with x
#   .find(x)        returns the position of x, or -1 if not found
#
# f-strings for formatting:
#   name = "ada"
#   print(f"Hello, {name.title()}!")  →  Hello, Ada!
#
# YOUR TASK
# ---------
# Clean a set of messy customer records, one field at a time.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# -----------------------------------------------------------------------------
# PART 1 — Clean up customer names
# -----------------------------------------------------------------------------
#
# These names came in from a web form — inconsistent capitalisation and
# extra spaces are common issues.
#
raw_names = [
    "  alice johnson  ",
    "BOB SMITH",
    "carol   white",
    "  DAVID lee",
]

print("--- Cleaned Names ---")

# 👉 YOUR CODE HERE: loop through raw_names, clean each one, and print it
# Each name should be stripped of whitespace and in Title Case
#
# Hint: you can chain methods:  name.strip().title()

for name in raw_names:
    clean_name = 
    print(clean_name)


# -----------------------------------------------------------------------------
# PART 2 — Standardise email addresses
# -----------------------------------------------------------------------------
#
# Email addresses should always be lowercase with no spaces.
#
raw_emails = [
    "Alice.Johnson@Example.COM",
    "  bob.smith@company.org  ",
    "CAROL.WHITE@BUSINESS.NET",
    "David.Lee@Corp.co.uk  ",
]

print("\n--- Cleaned Emails ---")

# 👉 YOUR CODE HERE: loop through raw_emails, clean each one, and print it
# Each email should be stripped and fully lowercase

for email in raw_emails:
    clean_email = 
    print(clean_email)


# -----------------------------------------------------------------------------
# PART 3 — Extract the domain from an email address
# -----------------------------------------------------------------------------
#
# Given an email address, pull out just the domain (the part after @).
#
# Hint: "alice@example.com".split("@")  →  ["alice", "example.com"]
#       The domain is at index [1]
#
email = "carol.white@business.net"

# 👉 YOUR CODE HERE: extract and print the domain

domain = 
print(f"\nDomain: {domain}")


# -----------------------------------------------------------------------------
# PART 4 — Build a formatted customer summary line
# -----------------------------------------------------------------------------
#
# Using your cleaned data, print one summary line per customer.
# It should look like this:
#
#   Alice Johnson | alice.johnson@example.com
#
# 👉 YOUR CODE HERE: use the first entries from raw_names and raw_emails
#    (clean them first), then print a formatted summary line



# =============================================================================
# STRETCH CHALLENGES
#
#   1. Check whether each email contains "@" using the in keyword or .find().
#      Print a warning for any email that doesn't look valid.
#
#   2. From a full name like "Alice Johnson", extract just the first name
#      and just the last name using .split().
#
#   3. Some customers wrote their phone numbers as "617-555-0192".
#      Use .replace() to reformat them as "(617) 555-0192".
# =============================================================================