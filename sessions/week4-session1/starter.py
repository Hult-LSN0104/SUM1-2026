# =============================================================================
# LSN-0104 | Week 4, Session 7
# Functions Part I — Modular Programming
# =============================================================================
#
# A function is a reusable, named block of code.
# Instead of writing the same logic over and over, you write it once
# and call it by name whenever you need it.
#
# Defining a function:
#   def function_name(parameter1, parameter2):
#       """Docstring: one line describing what this function does."""
#       # code goes here
#       return result
#
# Calling a function:
#   result = function_name(value1, value2)
#
# Default parameters (used when caller doesn't provide a value):
#   def greet(name, greeting="Hello"):
#       return f"{greeting}, {name}!"
#
#   greet("Alice")            →  "Hello, Alice!"
#   greet("Alice", "Hi")      →  "Hi, Alice!"
#
# The DRY principle: Don't Repeat Yourself.
# If you write the same logic twice, it belongs in a function.
#
# YOUR TASK
# ---------
# Remember the invoice calculator from Session 2? It was all written
# in one block. Today you'll break it into clean, reusable functions.
# This is called REFACTORING — improving structure without changing behaviour.
#
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# -----------------------------------------------------------------------------
# PART 1 — A function to calculate the line total
# -----------------------------------------------------------------------------
#
# Write a function called calculate_total that takes:
#   price     (float)  — unit price
#   quantity  (int)    — number of units
# and returns the total (price * quantity) as a float.
#
# 👉 YOUR CODE HERE

def calculate_total(price, quantity):
    """Calculate and return the total price for a given quantity."""
    


# -----------------------------------------------------------------------------
# PART 2 — A function to apply a discount
# -----------------------------------------------------------------------------
#
# Write a function called apply_discount that takes:
#   total            (float) — the original total
#   discount_percent (float) — the discount as a percentage (e.g. 10 for 10%)
#                              default value: 0  (no discount)
# and returns the discounted total.
#
# 👉 YOUR CODE HERE

def apply_discount(total, discount_percent=0):
    """Return the total after applying a percentage discount."""
    


# -----------------------------------------------------------------------------
# PART 3 — A function to format a currency value
# -----------------------------------------------------------------------------
#
# Write a function called format_currency that takes:
#   amount  (float) — any monetary value
# and returns a string formatted as a dollar amount with 2 decimal places.
# Example:  format_currency(1234.5)  →  "$1,234.50"
#
# 👉 YOUR CODE HERE

def format_currency(amount):
    """Return a dollar-formatted string for any monetary amount."""
    


# -----------------------------------------------------------------------------
# PART 4 — A function to print an invoice line
# -----------------------------------------------------------------------------
#
# Write a function called print_invoice_line that takes:
#   product_name     (str)
#   price            (float)
#   quantity         (int)
#   discount_percent (float) — default 0
# and prints one formatted invoice line. It should call your functions
# from Parts 1, 2, and 3 rather than doing the maths itself.
#
# Example output:
#   Laptop Stand    4 x $29.99  =  $119.96  (after 10% discount: $107.96)
#
# 👉 YOUR CODE HERE

def print_invoice_line(product_name, price, quantity, discount_percent=0):
    """Print a single formatted invoice line."""
    


# -----------------------------------------------------------------------------
# PART 5 — Put it all together
# -----------------------------------------------------------------------------
#
# Call print_invoice_line() three times with different products.
# At least one should have a discount applied.
#
# 👉 YOUR CODE HERE

print("--- Invoice ---")
print_invoice_line("Laptop Stand",    29.99,  4,  discount_percent=10)
print_invoice_line("Wireless Mouse",  19.99,  )
print_invoice_line(                                                    )


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Write a function called calculate_tax(total, tax_rate=0.08) that
#      returns the total including tax. Call it in your invoice.
#
#   2. Write a function called invoice_summary(items) that accepts a list
#      of (product, price, quantity) tuples and prints a full invoice
#      including a grand total line at the bottom.
#
#   3. What happens if someone calls apply_discount(100, 110) — a discount
#      greater than 100%? Add a check inside the function that prevents
#      the discounted price from going below zero.
# =============================================================================