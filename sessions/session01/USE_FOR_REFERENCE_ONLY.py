# =============================================================================
# LSN-0104 | Week 1, Session 2
# Basic Syntax, Variables, and Data Types
# =============================================================================
#
# In this session you'll work with variables and Python's core data types:
#   str   — text, always wrapped in quotes:         "hello"
#   int   — whole numbers:                          42
#   float — decimal numbers:                        9.99
#   bool  — True or False (capital T and F):        True
#
# You'll also practise converting between types:
#   int("5")    → 5
#   float("3")  → 3.0
#   str(100)    → "100"
#
# YOUR TASK
# ---------
# Build a simple invoice calculator, step by step.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# -----------------------------------------------------------------------------
# PART 1 — Store some product information in variables
# -----------------------------------------------------------------------------
#
# Create three variables:
#   product_name  — a string with the name of any product (e.g. "Laptop Stand")
#   price         — a float with the unit price  (e.g. 29.99)
#   quantity      — an integer with how many units (e.g. 4)
#
# 👉 YOUR CODE HERE: create the three variables below

product_name = 
price = 
quantity = 


# -----------------------------------------------------------------------------
# PART 2 — Calculate the total
# -----------------------------------------------------------------------------
#
# Multiply price by quantity and store the result in a new variable: total
#
# 👉 YOUR CODE HERE

total = 


# -----------------------------------------------------------------------------
# PART 3 — Print a formatted invoice line
# -----------------------------------------------------------------------------
#
# Use an f-string to print a single line that looks like this:
#
#   Invoice: 4 x Laptop Stand @ $29.99 each = $119.96
#
# Hint: to control how many decimal places a float shows, use :.2f inside { }
#   Example:  f"${price:.2f}"  →  "$29.99"
#
# 👉 YOUR CODE HERE

print(f"Invoice: ")


# -----------------------------------------------------------------------------
# PART 4 — Check your data types
# -----------------------------------------------------------------------------
#
# type() tells you what type a variable is.
# print(type(price)) will show: <class 'float'>
#
# 👉 YOUR CODE HERE: print the type of each of your three variables

print(type(product_name))


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Add a discount_percent variable (e.g. 10 for 10%) and calculate
#      a discounted total. Print both the original and discounted price.
#
#   2. Ask the user to type in the product name, price, and quantity
#      using input(). Remember: input() always returns a string,
#      so you'll need float() and int() to convert the numbers.
#
#   3. What happens if quantity is stored as a string "4" instead of
#      an integer 4? Try it and see what error you get.
# =============================================================================