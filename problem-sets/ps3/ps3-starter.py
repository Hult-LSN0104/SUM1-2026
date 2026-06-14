"""
LSN-0104 — Introduction to Programming with Python
Problem Set 3: Data Collections & File Handling

Author: <Abigail Adugna>
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
       if not items:
            print("Inventory is empty.")
            return
    
      print("\n--- CURRENT INVENTORY ---")
    
      for item in items:
          total_value = item["quantity"] * item["unit_price"]
          print(f"Name: {item['name']}")
          print(f"  SKU: {item['sku']}")
          print(f"  Quantity: {item['quantity']}")
          print(f"  Unit Price: ${item['unit_price']:.2f}")
          print(f"  Total Value: ${total_value:.2f}")
          print()



def add_item(items):
    """Prompt the user for name, sku, quantity, unit_price; append to items."""
    print("\n--- ADD NEW ITEM ---")
    
    try:
        name = input("Item name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        sku = input("SKU: ").strip()
        if not sku:
            print("Error: SKU cannot be empty.")
            return
        
        if any(item["sku"] == sku for item in items):
            print(f"Error: Item with SKU '{sku}' already exists.")
            return
        
        quantity_str = input("Quantity: ").strip()
        quantity = int(quantity_str)
        if quantity < 0:
            print("Error: Quantity must be non-negative.")
            return
        
        price_str = input("Unit Price: $").strip()
        unit_price = float(price_str)
        if unit_price < 0:
            print("Error: Price must be non-negative.")
            return
        
        items.append({
            "name": name,
            "sku": sku,
            "quantity": quantity,
            "unit_price": unit_price
        })
        print(f"✓ Item '{name}' added successfully.")
    
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers for quantity and price.")



def remove_item(items, sku):
    """Remove the item with the given SKU. Print a message if not found."""
    initial_length = len(items)
    items_to_keep = [item for item in items if item["sku"] != sku]
    
    if len(items_to_keep) < initial_length:
        items.clear()
        items.extend(items_to_keep)
        print(f"✓ Item with SKU '{sku}' removed successfully.")
    else:
        print(f"Error: No item found with SKU '{sku}'.")



def update_quantity(items, sku, new_quantity):
    """Update the quantity for the item with the given SKU."""
  if new_quantity < 0:
        print("Error: Quantity must be non-negative.")
        return False
    
    for item in items:
        if item["sku"] == sku:
            item["quantity"] = new_quantity
            print(f"✓ Quantity for '{item['name']}' updated to {new_quantity}.")
            return True
    
    print(f"Error: No item found with SKU '{sku}'.")
    return False



def total_value(items):
    """Return the sum of (quantity * unit_price) across all items."""
     total = sum(item["quantity"] * item["unit_price"] for item in items)
    return total


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

       while True:
        print("\n===== INVENTORY MANAGER =====")
        print("1. View all items")
        print("2. Add new item")
        print("3. Remove item by SKU")
        print("4. Update quantity by SKU")
        print("5. Show total inventory value")
        print("6. Exit")
        
        choice = input("Choice: ").strip()

        if choice == "1":
            view_items(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            sku = input("Enter SKU to remove: ").strip()
            remove_item(inventory, sku)
        elif choice == "4":
            sku = input("Enter SKU to update: ").strip()
            try:
                new_qty = int(input("New quantity: ").strip())
                update_quantity(inventory, sku, new_qty)
            except ValueError:
                print("Error: Please enter a valid number for quantity.")
        elif choice == "5":
            total = total_value(inventory)
            print(f"\nTotal Inventory Value: ${total:.2f}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")



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
    print("\n--- CUSTOMER SUMMARIES ---\n")
    
    for customer_id, customer_info in customers.items():
        purchases = customer_info["purchases"]
        total_spent = sum(purchases)
        avg_purchase = total_spent / len(purchases) if purchases else 0
        
        print(f"ID: {customer_id} | {customer_info['name']}")
        print(f"  Email: {customer_info['email']}")
        print(f"  Tier: {customer_info['tier']}")
        print(f"  Total Spent: ${total_spent:.2f}")
        print(f"  Average Purchase: ${avg_purchase:.2f}")
        print()

def find_top_customer(customers):
    """
    Return the customer ID of the customer with the highest total spending.
    Use .values() or .items() somewhere in your solution.
    """
   return max(customers, key=lambda cid: sum(customers[cid]["purchases"]))


def upgrade_to_gold(customers):
    """
    Upgrade any customer with total spending > $5,000 to 'Gold' tier.
    Use .keys() somewhere in your solution.
    """
    upgraded_count = 0
    
    for customer_id in customers.keys():
        total_spent = sum(customers[customer_id]["purchases"])
        if total_spent > 5000 and customers[customer_id]["tier"] != "Gold":
            customers[customer_id]["tier"] = "Gold"
            upgraded_count += 1
            print(f"✓ {customers[customer_id]['name']} upgraded to Gold tier!")
    
    if upgraded_count == 0:
        print("No customers qualified for upgrade.")


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
    records = []

    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["quantity"]   = int(row["quantity"])
            row["unit_price"] = float(row["unit_price"])
            row["revenue"]    = row["quantity"] * row["unit_price"]
            records.append(row)

    return records


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
    total_revenue   = sum(r["revenue"] for r in records)
    average_revenue = total_revenue / len(records) if records else 0

    rep_totals = {}
    for r in records:
        rep_totals[r["rep_name"]] = rep_totals.get(r["rep_name"], 0) + r["revenue"]

    top_rep_name = max(rep_totals, key=lambda name: rep_totals[name])
    top_rep = {"name": top_rep_name, "revenue": rep_totals[top_rep_name]}

    revenue_by_region = {}
    for r in records:
        revenue_by_region[r["region"]] = revenue_by_region.get(r["region"], 0) + r["revenue"]

    product_units = {}
    for r in records:
        product_units[r["product"]] = product_units.get(r["product"], 0) + r["quantity"]

    best_product_name = max(product_units, key=lambda p: product_units[p])
    best_product = {"name": best_product_name, "units_sold": product_units[best_product_name]}

    return {
        "total_revenue":     total_revenue,
        "average_revenue":   average_revenue,
        "top_rep":           top_rep,
        "revenue_by_region": revenue_by_region,
        "best_product":      best_product,
    }


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
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "w") as f:
        f.write("================================\n")
        f.write("   SALES PERFORMANCE REPORT\n")
        f.write(f"   Generated: {timestamp}\n")
        f.write("================================\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write(f"  Total Revenue:   ${stats['total_revenue']:,.2f}\n")
        f.write(f"  Average Sale:    ${stats['average_revenue']:,.2f}\n\n")

        f.write("REGIONAL BREAKDOWN\n")
        for region, revenue in stats["revenue_by_region"].items():
            f.write(f"  {region:<10} ${revenue:,.2f}\n")
        f.write("\n")

        f.write(f"TOP PERFORMER:  {stats['top_rep']['name']} — ${stats['top_rep']['revenue']:,.2f}\n")
        f.write(f"BEST PRODUCT:   {stats['best_product']['name']} ({stats['best_product']['units_sold']} units sold)\n")


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
     records = load_sales(CSV_PATH)
     print(f"Loaded {len(records)} records")
     stats = analyze_sales(records)
     write_report(stats, REPORT_PATH)
     print(f"Report written to {REPORT_PATH}")

