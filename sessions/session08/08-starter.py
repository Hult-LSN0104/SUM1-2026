# =============================================================================
# LSN-0104 | Week 5, Session 9
# Lists and Tuples — Managing Collections
# =============================================================================
#
# A LIST is an ordered, changeable collection:
#   fruits = ["apple", "banana", "cherry"]
#   fruits[0]           →  "apple"       (index from 0)
#   fruits[-1]          →  "cherry"      (last item)
#   fruits[0:2]         →  ["apple", "banana"]  (slice)
#
# Useful list methods:
#   .append(x)    add x to the end
#   .remove(x)    remove the first occurrence of x
#   .sort()       sort in place (alphabetically or numerically)
#   .reverse()    reverse in place
#   len(list)     number of items
#   x in list     True if x is in the list
#
# A TUPLE is an ordered, UNCHANGEABLE collection — use for data
# that should never be modified (e.g. a product code + name pair):
#   product = ("SKU-001", "Laptop Stand", 29.99)
#   product[0]    →  "SKU-001"
#
# YOUR TASK
# ---------
# Build an inventory manager for a small warehouse.
# A menu loop will let the user add, remove, and view stock.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# Starting inventory — each item is a tuple: (sku, name, quantity, price)
# Tuples are used here because SKU and name should not change.
inventory = [
    ("SKU-001", "Laptop Stand",   45, 29.99),
    ("SKU-002", "Wireless Mouse", 120, 19.99),
    ("SKU-003", "USB-C Hub",      33, 49.99),
    ("SKU-004", "Webcam HD",      18, 79.99),
    ("SKU-005", "Desk Lamp",      62, 34.99),
]


# -----------------------------------------------------------------------------
# PART 1 — A function to display the inventory
# -----------------------------------------------------------------------------
#
# Write a function called show_inventory that takes the inventory list
# and prints each item in a formatted table. Example:
#
#   SKU       Name              Qty    Price
#   ----------------------------------------
#   SKU-001   Laptop Stand       45   $29.99
#   SKU-002   Wireless Mouse    120   $19.99
#
# 👉 YOUR CODE HERE

def show_inventory(inv):
    """Print the full inventory as a formatted table."""
    print(f"\n{'SKU':<10}{'Name':<20}{'Qty':>5}  {'Price':>8}")
    print("-" * 46)
    for item in inv:
        sku, name, qty, price = item
        


# -----------------------------------------------------------------------------
# PART 2 — A function to add a new item
# -----------------------------------------------------------------------------
#
# Write a function called add_item that takes the inventory list and:
#   - asks the user for SKU, name, quantity, and price
#   - creates a new tuple with those values
#   - appends it to the inventory list
#   - prints a confirmation message
#
# Note: lists are mutable, so changes inside the function affect the original.
#
# 👉 YOUR CODE HERE

def add_item(inv):
    """Prompt the user for details and add a new item to the inventory."""
    sku   = input("SKU: ").strip().upper()
    name  = input("Product name: ").strip()
    qty   = int(input("Quantity: "))
    price = float(input("Unit price: $"))
    
    new_item = 
    inv.append(new_item)
    print(f"✓ Added {name} to inventory.")


# -----------------------------------------------------------------------------
# PART 3 — A function to remove an item by SKU
# -----------------------------------------------------------------------------
#
# Write a function called remove_item that takes the inventory list and:
#   - asks the user for a SKU
#   - searches the inventory for a matching SKU
#   - removes it if found, prints a message either way
#
# Hint: loop through the list with a for loop, check item[0] == sku,
#       then use inv.remove(item) and break.
#
# 👉 YOUR CODE HERE

def remove_item(inv):
    """Remove an inventory item by SKU."""
    sku = input("Enter SKU to remove: ").strip().upper()
    for item in inv:
        if item[0] == sku:
            
            print(f"✓ Removed {item[1]} from inventory.")
            return
    print(f"SKU {sku} not found.")


# -----------------------------------------------------------------------------
# PART 4 — A function to find low-stock items
# -----------------------------------------------------------------------------
#
# Write a function called check_low_stock that takes:
#   inv        (list)  — the inventory
#   threshold  (int)   — flag items at or below this quantity, default 20
# and prints any items that need reordering.
#
# 👉 YOUR CODE HERE

def check_low_stock(inv, threshold=20):
    """Print a warning for any items at or below the stock threshold."""
    print(f"\n--- Low Stock Alert (threshold: {threshold} units) ---")
    found_any = False
    for item in inv:
        sku, name, qty, price = item
        if :
            print(f"⚠️  {name} ({sku}): only {qty} units left")
            found_any = True
    if not found_any:
        print("All items are adequately stocked.")


# -----------------------------------------------------------------------------
# PART 5 — The main menu loop
# -----------------------------------------------------------------------------
#
# Run a loop that displays a menu and calls the right function.
# Keep looping until the user chooses to quit.
#
# Menu options:
#   1 — View inventory
#   2 — Add item
#   3 — Remove item
#   4 — Check low stock
#   5 — Quit
#
# 👉 YOUR CODE HERE

print("=== Inventory Manager ===")

while True:
    print("\nWhat would you like to do?")
    print("  1 — View inventory")
    print("  2 — Add item")
    print("  3 — Remove item")
    print("  4 — Check low stock")
    print("  5 — Quit")
    
    choice = input("Enter choice (1–5): ").strip()
    
    if choice == "1":
        show_inventory(inventory)
    elif choice == "2":
        
    elif choice == "3":
        
    elif choice == "4":
        
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice — please enter a number from 1 to 5.")


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Add an "Update quantity" option to the menu. Ask for a SKU and
#      a new quantity, find the item, and replace it with an updated tuple.
#      (Hint: tuples can't be changed — you'll need to create a new one.)
#
#   2. Calculate and print the total inventory value:
#      sum of (quantity * price) for every item.
#
#   3. Sort the inventory by quantity (lowest first) before displaying it.
#      Hint: sorted(inv, key=lambda item: item[2])
# =============================================================================