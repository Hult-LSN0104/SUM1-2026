"""
LSN-0104 — Introduction to Programming with Python
Problem Set 1: Variables, Data Types & Strings

Author: <your name here>

Notes:
  - Each exercise is a separate section. As you work, you can comment out
    sections you're not testing yet so input() prompts don't pile up.
  - Currency should be displayed with a `$` and 2 decimal places.
"""

import math


# =============================================================================
# Exercise 1 — Hello, Business World! (10 pts)
# =============================================================================
# TODO:
#   - Ask the user for first name, last name, and company name using input()
#   - Print the greeting: "Hello, [First] [Last] from [Company]! Welcome to Python."
#   - Print the full name in ALL CAPS
#   - Print the company name in Title Case
#   - Print the total number of characters in the full name (incl. the space)

print("\n===== Exercise 1: Hello, Business World! =====")

# first_name = input("First name: ")
# last_name  = input("Last name: ")
# company    = input("Company name: ")

# Your code here


# =============================================================================
# Exercise 2 — Invoice Calculator (20 pts)
# =============================================================================
# TODO:
#   - Ask for product name (str), unit price (float), and quantity (int)
#   - Calculate subtotal, tax (8%), and total
#   - Print a formatted invoice — use at least one f-string
#   - All currency values formatted with $ and 2 decimal places

print("\n===== Exercise 2: Invoice Calculator =====")

# product  = input("Product name: ")
# price    = float(input("Unit price: "))
# quantity = int(input("Quantity: "))

# Your code here


# =============================================================================
# Exercise 3 — Customer Data Cleaner (20 pts)
# =============================================================================
# TODO:
#   - Strip whitespace from name and email
#   - Convert name to Title Case; convert email to lowercase
#   - If email ends with "@company.com" -> "Internal employee", else "External contact"
#   - Extract the area code (first 3 digits inside the parentheses)
#   - Print a clean, formatted customer card showing all cleaned values

print("\n===== Exercise 3: Customer Data Cleaner =====")

raw_name  = "  jANe  dOe  "
raw_email = "  Jane.Doe@COMPANY.COM  "
raw_phone = "(617) 555-0142"

# Your code here


# =============================================================================
# Exercise 4 — Profit Margin Calculator (10 pts)
# =============================================================================
# TODO:
#   - Ask for revenue and cost of goods sold (COGS)
#   - Calculate gross profit (revenue - COGS)
#   - Calculate gross margin % ((gross profit / revenue) * 100)
#   - Use math.ceil() and math.floor() on the margin %
#   - Format output with 2 decimal places and a % symbol
#
# BONUS (+5 pts):
#   - Use round() to also display a rounded margin
#   - Add a comment explaining when rounding vs. truncating matters in finance

print("\n===== Exercise 4: Profit Margin Calculator =====")

# revenue = float(input("Revenue: "))
# cogs    = float(input("Cost of goods sold (COGS): "))

# Your code here