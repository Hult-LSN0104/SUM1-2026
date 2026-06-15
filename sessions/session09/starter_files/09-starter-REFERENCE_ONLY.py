# =============================================================================
# LSN-0104 | Week 5, Session 10
# Dictionaries — Key-Value Data Structures
# =============================================================================
#
# A DICTIONARY stores data as key-value pairs.
# Think of it like a real dictionary: you look up a word (key)
# to get its definition (value).
#
#   customer = {
#       "name": "Alice Johnson",
#       "email": "alice@example.com",
#       "tier": "Gold"
#   }
#
# Accessing values:
#   customer["name"]              →  "Alice Johnson"
#   customer.get("phone", "N/A")  →  "N/A"  (safe — no crash if key missing)
#
# Adding / updating:
#   customer["phone"] = "617-555-0101"
#   customer["tier"]  = "Platinum"
#
# Removing:
#   del customer["phone"]
#
# Iterating:
#   for key in customer:                     # keys only
#   for key, value in customer.items():      # both
#   for value in customer.values():          # values only
#
# Nested dictionaries — a dictionary inside a dictionary:
#   customers = {
#       "C001": {"name": "Alice", "email": "alice@example.com"},
#       "C002": {"name": "Bob",   "email": "bob@example.com"},
#   }
#   customers["C001"]["name"]   →   "Alice"
#
# YOUR TASK
# ---------
# Build a customer profile manager using a nested dictionary.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# Starting data — a dictionary of customers keyed by customer ID
# Each customer has a name, email, tier, and purchase history (a list)
customers = {
    "C001": {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "tier": "Gold",
        "purchases": [250.00, 89.99, 430.00, 125.50]
    },
    "C002": {
        "name": "Bob Smith",
        "email": "bob@example.com",
        "tier": "Standard",
        "purchases": [45.00, 67.50]
    },
    "C003": {
        "name": "Carol White",
        "email": "carol@example.com",
        "tier": "Platinum",
        "purchases": [1200.00, 850.00, 2100.00, 475.00, 990.00]
    },
}


# -----------------------------------------------------------------------------
# PART 1 — A function to display one customer's profile
# -----------------------------------------------------------------------------
#
# Write a function called show_customer that takes:
#   customer_id  (str)  — the key, e.g. "C001"
#   customers    (dict) — the full customers dictionary
# and prints the customer's details including:
#   - name, email, tier
#   - number of purchases
#   - total spend
#   - average purchase value
#
# If the ID is not found, print a "not found" message.
#
# 👉 YOUR CODE HERE

def show_customer(customer_id, customers):
    """Display a formatted profile for a single customer."""
    if customer_id not in customers:
        print(f"Customer {customer_id} not found.")
        return
    
    c = customers[customer_id]
    total_spend = 
    avg_purchase = 
    
    print(f"\n--- Customer Profile: {customer_id} ---")
    print(f"Name:        {c['name']}")
    print(f"Email:       {c['email']}")
    print(f"Tier:        {c['tier']}")
    print(f"Purchases:   {len(c['purchases'])}")
    print(f"Total Spend: ${total_spend:,.2f}")
    print(f"Average:     ${avg_purchase:,.2f}")


# -----------------------------------------------------------------------------
# PART 2 — A function to add a new purchase to a customer's history
# -----------------------------------------------------------------------------
#
# Write a function called add_purchase that takes:
#   customer_id  (str)
#   amount       (float)
#   customers    (dict)
# and appends the amount to that customer's purchases list.
# Print a confirmation. Handle the case where the ID doesn't exist.
#
# 👉 YOUR CODE HERE

def add_purchase(customer_id, amount, customers):
    """Record a new purchase for an existing customer."""
    


# -----------------------------------------------------------------------------
# PART 3 — A function to add a brand new customer
# -----------------------------------------------------------------------------
#
# Write a function called add_customer that takes:
#   customers    (dict)
# Prompts the user for: customer ID, name, email, tier
# Creates a new customer dictionary with an empty purchases list
# Adds it to customers. Warn if the ID already exists.
#
# 👉 YOUR CODE HERE

def add_customer(customers):
    """Prompt for details and add a new customer to the directory."""
    customer_id = input("Customer ID (e.g. C004): ").strip().upper()
    
    if customer_id in customers:
        print(f"Customer {customer_id} already exists.")
        return
    
    name  = input("Name: ").strip()
    email = input("Email: ").strip().lower()
    tier  = input("Tier (Standard / Gold / Platinum): ").strip().title()
    
    customers[customer_id] = {
        
    }
    print(f"✓ Customer {name} added.")


# -----------------------------------------------------------------------------
# PART 4 — A function to list all customers with their total spend
# -----------------------------------------------------------------------------
#
# Write a function called list_all_customers that takes customers (dict)
# and prints a summary table of all customers sorted by total spend,
# highest first.
#
# Example:
#   ID      Name              Tier        Total Spend
#   --------------------------------------------------
#   C003    Carol White       Platinum    $5,615.00
#   C001    Alice Johnson     Gold        $  895.49
#   C002    Bob Smith         Standard    $  112.50
#
# Hint: sorted(customers.items(), key=lambda x: sum(x[1]["purchases"]), reverse=True)
#
# 👉 YOUR CODE HERE

def list_all_customers(customers):
    """Print all customers sorted by total spend, highest first."""
    print(f"\n{'ID':<8}{'Name':<20}{'Tier':<12}{'Total Spend':>12}")
    print("-" * 54)
    
    sorted_customers = sorted(
        customers.items(),
        key=lambda x: sum(x[1]["purchases"]),
        reverse=True
    )
    
    for customer_id, c in sorted_customers:
        total = 
        print(f"")


# -----------------------------------------------------------------------------
# PART 5 — The main menu loop
# -----------------------------------------------------------------------------
#
# Build a menu with options:
#   1 — View all customers
#   2 — View customer profile (by ID)
#   3 — Add new purchase
#   4 — Add new customer
#   5 — Quit
#
# 👉 YOUR CODE HERE

print("=== Customer Profile Manager ===")

while True:
    print("\n1 — View all customers")
    print("2 — View customer profile")
    print("3 — Add purchase")
    print("4 — Add new customer")
    print("5 — Quit")
    
    choice = input("Choice: ").strip()
    
    if choice == "1":
        list_all_customers(customers)
    elif choice == "2":
        cid = input("Customer ID: ").strip().upper()
        show_customer(cid, customers)
    elif choice == "3":
        cid    = input("Customer ID: ").strip().upper()
        amount = float(input("Purchase amount: $"))
        add_purchase(cid, amount, customers)
    elif choice == "4":
        add_customer(customers)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please enter 1–5.")


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Add a function that automatically upgrades a customer's tier based
#      on their total spend:
#        < $500        → Standard
#        $500–$2,000   → Gold
#        > $2,000      → Platinum
#
#   2. Add a "search by name" option that finds customers whose name
#      contains the text the user types (case-insensitive).
#
#   3. Add a function that removes a customer by ID, with a confirmation
#      prompt before deleting ("Are you sure? yes/no").
# =============================================================================