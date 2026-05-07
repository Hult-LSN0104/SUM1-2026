# =============================================================================
# LSN-0104 | Problem Set 3 — Shipping Cost Calculator
# =============================================================================
#
# Instructions are in instructions.md
# Read the shipping rules carefully before writing any code.
# =============================================================================

# The orders — do not change this data
orders = [
    {"id": "ORD-101", "customer": "Alice Johnson",  "destination": "domestic",      "weight_kg": 2.5,  "service": "standard",  "product_value": 89.99},
    {"id": "ORD-102", "customer": "Bob Smith",      "destination": "international", "weight_kg": 0.8,  "service": "express",   "product_value": 45.00},
    {"id": "ORD-103", "customer": "Carol White",    "destination": "domestic",      "weight_kg": 35.0, "service": "standard",  "product_value": 320.00},
    {"id": "ORD-104", "customer": "David Lee",      "destination": "domestic",      "weight_kg": 1.2,  "service": "overnight", "product_value": 59.99},
    {"id": "ORD-105", "customer": "Elena Garcia",   "destination": "international", "weight_kg": 5.0,  "service": "overnight", "product_value": 199.00},
    {"id": "ORD-106", "customer": "Frank Nguyen",   "destination": "domestic",      "weight_kg": 0.4,  "service": "express",   "product_value": 250.00},
    {"id": "ORD-107", "customer": "Grace Kim",      "destination": "international", "weight_kg": 12.0, "service": "standard",  "product_value": 780.00},
    {"id": "ORD-108", "customer": "Henry Patel",    "destination": "domestic",      "weight_kg": 28.0, "service": "overnight", "product_value": 145.00},
]

# Shipping rates — store these as constants so your logic can reference them
DOMESTIC_RATES      = {"standard": 0.80, "express": 1.50, "overnight": 3.00}
INTL_RATES          = {"standard": 2.50, "express": 4.00}
HEAVY_SURCHARGE     = 25.00
CUSTOMS_FEE         = 15.00
FREE_SHIPPING_MIN   = 200.00
HEAVY_WEIGHT_LIMIT  = 30.0
MIN_WEIGHT          = 1.0


# -----------------------------------------------------------------------------
# STEP 1 — Process each order
# -----------------------------------------------------------------------------
# Loop through orders and calculate the shipping cost for each one.
# Apply all rules from the instructions.
# Print one summary line per order.

# 👉 YOUR CODE HERE

total_shipping_revenue = 0.0

print(f"{'ID':<9}{'Customer':<20}{'Dest':<8}{'Service':<11}{'Weight':>7}{'Shipping':>10}  Notes")
print("-" * 80)

for order in orders:
    order_id      = order["id"]
    customer      = order["customer"]
    destination   = order["destination"]
    weight        = order["weight_kg"]
    service       = order["service"]
    product_value = order["product_value"]
    notes         = []

    # Apply minimum weight
    if weight < MIN_WEIGHT:
        weight = MIN_WEIGHT
        notes.append("min 1kg applied")

    # Check for invalid overnight + international
    if :
        notes.append("overnight unavailable intl — billed as express")
        service = "express"

    # Calculate base shipping cost
    if destination == "domestic":
        base_cost = 
    else:
        base_cost = 

    # Apply surcharges
    surcharge = 0.0
    if :
        surcharge += HEAVY_SURCHARGE
        notes.append("heavy surcharge")
    if destination == "international":
        surcharge += CUSTOMS_FEE
        notes.append(f"customs ${CUSTOMS_FEE:.2f}")

    # Apply free shipping (waives base cost only)
    free_shipping = False
    if :
        free_shipping = True
        notes.append("FREE shipping (order > $200)")

    # Calculate final cost
    if free_shipping:
        shipping_cost = surcharge
    else:
        shipping_cost = base_cost + surcharge

    total_shipping_revenue += shipping_cost

    dest_label = "intl" if destination == "international" else "domestic"
    notes_str  = ", ".join(notes) if notes else ""
    print(f"{order_id:<9}{customer:<20}{dest_label:<8}{service:<11}{weight:>5.1f}kg  ${shipping_cost:>7.2f}  {notes_str}")


# -----------------------------------------------------------------------------
# STEP 2 — Print the totals section
# -----------------------------------------------------------------------------

# 👉 YOUR CODE HERE
print("-" * 80)
print(f"Total shipping revenue collected: $")
