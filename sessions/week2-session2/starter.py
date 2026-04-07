# =============================================================================
# LSN-0104 | Week 2, Session 4
# Working with Numbers and Business Calculations
# =============================================================================
#
# Python arithmetic operators:
#   +   addition          10 + 3  →  13
#   -   subtraction       10 - 3  →  7
#   *   multiplication    10 * 3  →  30
#   /   division          10 / 3  →  3.333...
#   //  floor division    10 // 3 →  3       (rounds down to whole number)
#   %   modulo            10 % 3  →  1       (remainder)
#   **  exponent          10 ** 2 →  100
#
# Useful built-in functions:
#   round(3.14159, 2)   →  3.14
#   abs(-5)             →  5
#
# The math module (must be imported first):
#   import math
#   math.floor(3.9)     →  3    (always rounds DOWN)
#   math.ceil(3.1)      →  4    (always rounds UP)
#
# f-string number formatting:
#   f"${value:.2f}"          →  "$9.99"    (2 decimal places)
#   f"{rate:.1%}"            →  "42.5%"    (percentage, 1 decimal)
#
# YOUR TASK
# ---------
# Build a profit margin calculator for a small product line.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================

import math


# -----------------------------------------------------------------------------
# PART 1 — Get inputs from the user
# -----------------------------------------------------------------------------
#
# Ask the user for:
#   product_name  — a string
#   revenue       — how much the product earned (float)
#   cost          — how much it cost to produce (float)
#
# Remember: input() always returns a string, so convert numbers with float()
#
# 👉 YOUR CODE HERE

product_name = input("Product name: ")
revenue = 
cost = 


# -----------------------------------------------------------------------------
# PART 2 — Calculate profit and margin
# -----------------------------------------------------------------------------
#
# profit        = revenue minus cost
# gross_margin  = profit divided by revenue  (this gives a decimal, e.g. 0.42)
#
# 👉 YOUR CODE HERE

profit = 
gross_margin = 


# -----------------------------------------------------------------------------
# PART 3 — Apply a discount and calculate the discounted price
# -----------------------------------------------------------------------------
#
# Ask the user for a discount percentage (e.g. they type 10 for 10%)
# Convert it to a decimal (divide by 100), then calculate:
#   discount_amount   = revenue * discount rate
#   discounted_price  = revenue - discount_amount
#
# Use math.floor() to round the discounted price DOWN to the nearest dollar.
# (Some retailers always round down so the customer pays less, not more.)
#
# 👉 YOUR CODE HERE

discount_percent = float(input("Discount percentage (e.g. 10 for 10%): "))
discount_rate = 
discount_amount = 
discounted_price = 
discounted_price_floored = 


# -----------------------------------------------------------------------------
# PART 4 — Print a formatted summary report
# -----------------------------------------------------------------------------
#
# Print a report that looks like this (your numbers will differ):
#
#   ---- Profit Report: Laptop Stand ----
#   Revenue:           $  250.00
#   Cost:              $  140.00
#   Profit:            $  110.00
#   Gross Margin:          44.0%
#   Discounted Price:  $  225.00  (after 10% discount)
#
# 👉 YOUR CODE HERE

print(f"\n---- Profit Report: {product_name} ----")
print(f"Revenue:          ${revenue:>9.2f}")


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Add a simple "health check": if gross_margin is below 20%, print
#      a warning that says "⚠️  Low margin — review pricing."
#      (You'll practice this properly in Session 5 with conditionals.)
#
#   2. Calculate how many units need to sell at the current price to
#      break even, given a fixed overhead cost the user enters.
#      Hint: units = math.ceil(overhead / price_per_unit)
#
#   3. Ask for 3 products and their revenues, then calculate and print
#      the total revenue across all three.
# =============================================================================