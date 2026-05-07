"""
LSN-0104 — Introduction to Programming with Python
Problem Set 3: Data Collections & File Handling

Author: <your name here>
"""

import csv
from datetime import datetime


# =============================================================================
# Exercise 1 — Inventory Manager (15 pts)
# =============================================================================

inventory = [
    {"name": "Widget Pro",   "sku": "WP-001", "quantity": 25, "unit_price": 19.99},
    {"name": "Gadget Plus",  "sku": "GP-002", "quantity": 10, "unit_price": 49.99},
    {"name": "Thingamajig",  "sku": "TJ-003", "quantity": 50, "unit_price":  4.99},
]


def view_items(items):
    """Print every item in the inventory in a readable format."""
    # TODO
    pass


def add_item(items):
    """Prompt the user for name, sku, quantity, unit_price; append to items."""
    # TODO
    pass


def remove_item(items, sku):
    """Remove the item with the given SKU. Print a message if not found."""
    # TODO
    pass


def update_quantity(items, sku, new_quantity):
    """Update the quantity for the item with the given SKU."""
    # TODO
    pass


def total_value(items):
    """Return the sum of (quantity * unit_price) across all items."""
    # TODO
    pass


def inventory_menu():
    """Run the menu loop until the user chooses to exit (option 6)."""
    while True:
        print("\n===== INVENTORY MANAGER =====")
        print("1. View all items")
        print("2. Add new item")
        print("3. Remove item by SKU")
        print("4. Update quantity by SKU")
        print("5. Show total inventory value")
        print("6. Exit")
        choice = input("Choice: ").strip()

        # TODO: dispatch on `choice`. Handle invalid input gracefully (no crashes).
        if choice == "6":
            print("Goodbye!")
            break


# =============================================================================
# Exercise 2 — Customer Profile Manager (15 pts)
# =============================================================================

customers = {
    "C001": {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "tier": "Silver",
        "purchases": [120.00, 89.50, 240.75],
    },
    "C002": {
        "name": "Bob Smith",
        "email": "bob@example.com",
        "tier": "Bronze",
        "purchases": [49.99, 19.99],
    },
    "C003": {
        "name": "Carol White",
        "email": "carol@example.com",
        "tier": "Silver",
        "purchases": [1500.00, 2200.00, 1800.00, 600.00],
    },
    "C004": {
        "name": "David Lee",
        "email": "david@example.com",
        "tier": "Bronze",
        "purchases": [75.00, 150.00, 95.50],
    },
}


def summarize_customers(customers):
    """
    Print a summary line for each customer:
        name, email, tier, total spent, average purchase.
    Use .items() somewhere in your solution.
    """
    # TODO
    pass


def find_top_customer(customers):
    """
    Return the customer ID of the customer with the highest total spending.
    Use .values() or .items() somewhere in your solution.
    """
    # TODO
    pass


def upgrade_to_gold(customers):
    """
    Upgrade any customer with total spending > $5,000 to 'Gold' tier.
    Use .keys() somewhere in your solution.
    """
    # TODO
    pass


# =============================================================================
# Exercise 3 — CSV Sales Processor (30 pts)
# =============================================================================
# Required CSV columns: date, rep_name, product, quantity, unit_price, region
# Create your own sales_data.csv with at least 15 rows across 3 regions and 3 reps.

CSV_PATH    = "sales_data.csv"
REPORT_PATH = "sales_report.txt"


# ---- Part A — Read and Parse (10 pts) ---------------------------------------

def load_sales(path):
    """
    Read the CSV at `path` using the csv module.
    Return a list of dicts, one per row, with these conversions applied:
        - quantity    -> int
        - unit_price  -> float
        - revenue     -> float (added field: quantity * unit_price)
    """
    # TODO: open(path, newline=""), use csv.DictReader, build the list
    pass


# ---- Part B — Analyze (10 pts) ----------------------------------------------

def analyze_sales(records):
    """
    Return a dict containing:
        total_revenue      (float)
        average_revenue    (float)
        top_rep            ({"name": str, "revenue": float})
        revenue_by_region  ({region_name: float, ...})
        best_product       ({"name": str, "units_sold": int})
    """
    # TODO
    pass


# ---- Part C — Write Report (10 pts) -----------------------------------------

def write_report(stats, path):
    """
    Write a human-readable report to `path` using the layout shown in the
    problem set instructions:
        - Section headers
        - Aligned columns
        - Currency formatted with $ and 2 decimal places
        - Generated timestamp
    """
    # TODO: open(path, "w") and write the formatted report
    pass


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    # ---- Exercise 1 ----
    # inventory_menu()

    # ---- Exercise 2 ----
    # summarize_customers(customers)
    # top_id = find_top_customer(customers)
    # print(f"Top customer: {top_id}")
    # upgrade_to_gold(customers)
    # summarize_customers(customers)  # show updated tiers

    # ---- Exercise 3 ----
    # records = load_sales(CSV_PATH)
    # print(f"Loaded {len(records)} records")
    # stats = analyze_sales(records)
    # write_report(stats, REPORT_PATH)
    # print(f"Report written to {REPORT_PATH}")

    pass