# =============================================================================
# LSN-0104 | Week 4, Session 8
# Functions Part II — Error Handling and Input Validation
# =============================================================================
#
# Real programs receive unexpected input. A user might type "abc" when
# you expected a number, or enter a negative price by accident.
# Without handling these cases, your program crashes.
#
# try / except — catch errors before they crash your program:
#   try:
#       result = int(input("Enter a number: "))
#   except ValueError:
#       print("That wasn't a number.")
#
# Common exception types:
#   ValueError     — wrong type (e.g. int("hello"))
#   ZeroDivisionError — dividing by zero
#   TypeError      — wrong operation for the type
#
# Docstrings — the first line inside a function, in triple quotes:
#   def my_function(x):
#       """What this function does, in one sentence."""
#       ...
#
# Functions calling other functions:
#   def get_subtotal(price, qty):
#       return price * qty
#
#   def get_total_with_tax(price, qty, tax_rate):
#       subtotal = get_subtotal(price, qty)   # calls the function above
#       return subtotal * (1 + tax_rate)
#
# YOUR TASK
# ---------
# Build a validated order-entry system. Each function you write
# will be called by the next one — a chain of small, testable pieces.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# -----------------------------------------------------------------------------
# PART 1 — A safe input function for positive numbers
# -----------------------------------------------------------------------------
#
# Write a function called get_positive_float that takes:
#   prompt  (str) — the message shown to the user
# and:
#   - asks the user for a number using input()
#   - uses try/except to catch ValueError if they type something non-numeric
#   - checks that the number is greater than zero
#   - keeps asking until it gets a valid positive number
#   - returns the number as a float
#
# 👉 YOUR CODE HERE

def get_positive_float(prompt):
    """Ask the user for a positive number, re-prompting on invalid input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                
        except ValueError:
            


# -----------------------------------------------------------------------------
# PART 2 — A safe input function for positive integers
# -----------------------------------------------------------------------------
#
# Write a similar function called get_positive_int.
# Same logic, but converts to int() and the value must be >= 1.
#
# 👉 YOUR CODE HERE

def get_positive_int(prompt):
    """Ask the user for a positive whole number, re-prompting on invalid input."""
    


# -----------------------------------------------------------------------------
# PART 3 — A function to build one order item
# -----------------------------------------------------------------------------
#
# Write a function called get_order_item that takes no parameters and:
#   - asks for a product name (string, cannot be blank)
#   - uses get_positive_float() to get the unit price
#   - uses get_positive_int() to get the quantity
#   - returns a dictionary: {"name": ..., "price": ..., "quantity": ...}
#
# 👉 YOUR CODE HERE

def get_order_item():
    """Collect and return one validated order item as a dictionary."""
    name = input("Product name: ").strip()
    while name == "":
        print("Product name cannot be blank.")
        name = 
    
    price = 
    quantity = 
    
    return {"name": name, "price": price, "quantity": quantity}


# -----------------------------------------------------------------------------
# PART 4 — A function to calculate and print an order summary
# -----------------------------------------------------------------------------
#
# Write a function called print_order_summary that takes:
#   items       (list of dicts) — your list of order items
#   tax_rate    (float)         — e.g. 0.08 for 8%   default: 0.08
# and prints a formatted summary:
#
#   ---- Order Summary ----
#   Laptop Stand     x4    $119.96
#   Wireless Mouse   x2    $ 39.98
#   ----------------------
#   Subtotal:              $159.94
#   Tax (8%):              $ 12.80
#   Total:                 $172.74
#
# 👉 YOUR CODE HERE

def print_order_summary(items, tax_rate=0.08):
    """Print a formatted order summary including tax."""
    print("\n---- Order Summary ----")
    subtotal = 0
    for item in items:
        line_total = 
        subtotal += line_total
        print(f"")
    
    tax = 
    total = 
    
    print(f"{'':->23}")
    print(f"Subtotal:    ${subtotal:>9.2f}")
    


# -----------------------------------------------------------------------------
# PART 5 — The main order-entry loop
# -----------------------------------------------------------------------------
#
# Write a loop that:
#   - calls get_order_item() to collect one item
#   - adds it to a list called `order`
#   - asks "Add another item? (yes/no)"
#   - stops when the user types anything other than "yes"
# Then calls print_order_summary(order).
#
# 👉 YOUR CODE HERE

order = []

print("=== New Order ===")
while True:
    item = get_order_item()
    order.append(item)
    again = input("Add another item? (yes/no): ").strip().lower()
    if again != "yes":
        

print_order_summary(order)


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Add a discount_percent field to get_order_item() — ask the user
#      for an optional discount per item and apply it in the summary.
#
#   2. Add a function called save_order(items, filename) that writes
#      the order to a .txt file. (Preview of Session 11!)
#
#   3. What happens if the user has an empty order (they immediately say "no")?
#      Add a check that prevents printing a summary for zero items.
# =============================================================================