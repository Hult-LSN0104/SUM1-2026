# =============================================================================
# LSN-0104 | Problem Set 5 — Product Catalogue Manager
# =============================================================================
#
# Instructions are in instructions.md
# =============================================================================

# Starting catalogue — do not change this data
catalogue = {
    "SKU-001": {"name": "Laptop Stand",       "category": "Accessories", "price": 29.99, "tags": ("ergonomic", "home office", "adjustable"), "stock": 45, "reviews": [4, 5, 3, 5, 4]},
    "SKU-002": {"name": "Wireless Mouse",      "category": "Peripherals", "price": 19.99, "tags": ("wireless", "compact", "home office"),     "stock": 120,"reviews": [3, 4, 4, 5, 3, 4]},
    "SKU-003": {"name": "USB-C Hub",           "category": "Peripherals", "price": 49.99, "tags": ("connectivity", "multi-port", "usb-c"),    "stock": 33, "reviews": [5, 5, 4, 4, 5]},
    "SKU-004": {"name": "Webcam HD",           "category": "Peripherals", "price": 79.99, "tags": ("video", "hd", "streaming"),               "stock": 18, "reviews": [4, 3, 4, 5]},
    "SKU-005": {"name": "Desk Lamp",           "category": "Furniture",   "price": 34.99, "tags": ("lighting", "adjustable", "home office"),  "stock": 62, "reviews": [4, 4, 5, 3, 4, 5]},
    "SKU-006": {"name": "Mechanical Keyboard", "category": "Peripherals", "price": 89.99, "tags": ("mechanical", "tactile", "rgb"),           "stock": 27, "reviews": [5, 5, 5, 4, 5]},
}


# -----------------------------------------------------------------------------
# FUNCTION 1 — display_catalogue
# -----------------------------------------------------------------------------

def display_catalogue(catalogue):
    """Print all products in a formatted table."""
    print(f"\n{'SKU':<10}{'Name':<25}{'Category':<14}{'Price':>8}{'Stock':>7}{'Avg ★':>7}")
    print("-" * 72)
    # 👉 YOUR CODE HERE
    for sku, product in catalogue.items():
        avg_rating = 
        print(f"")


# -----------------------------------------------------------------------------
# FUNCTION 2 — search_by_tag
# -----------------------------------------------------------------------------

def search_by_tag(catalogue, tag):
    """Return and print products whose tags include the given tag."""
    # 👉 YOUR CODE HERE
    results = []
    for sku, product in catalogue.items():
        if :
            results.append(sku)
    
    if results:
        print(f"\nResults for tag '{tag}':")
        for sku in results:
            print(f"  {sku} — {catalogue[sku]['name']}")
    else:
        print(f"No results found for tag '{tag}'.")
    
    return results


# -----------------------------------------------------------------------------
# FUNCTION 3 — add_review
# -----------------------------------------------------------------------------

def add_review(catalogue, sku, rating):
    """Add a rating to a product's reviews list."""
    # 👉 YOUR CODE HERE
    if sku not in catalogue:
        
        return
    if not isinstance(rating, int) or rating < 1 or rating > 5:
        
        return
    
    catalogue[sku]["reviews"].append(rating)
    print(f"✓ Review ({rating}★) added for {catalogue[sku]['name']}.")


# -----------------------------------------------------------------------------
# FUNCTION 4 — apply_category_discount
# -----------------------------------------------------------------------------

def apply_category_discount(catalogue, category, discount_percent):
    """Apply a percentage discount to all products in a category."""
    # 👉 YOUR CODE HERE
    print(f"\nApplying {discount_percent}% discount to all '{category}' products:")
    updated = 0
    for sku, product in catalogue.items():
        if product["category"] == category:
            old_price = product["price"]
            new_price = 
            product["price"] = round(new_price, 2)
            print(f"  {product['name']:<25} ${old_price:.2f} → ${product['price']:.2f}")
            updated += 1
    if updated == 0:
        print(f"  No products found in category '{category}'.")


# -----------------------------------------------------------------------------
# FUNCTION 5 — low_stock_report
# -----------------------------------------------------------------------------

def low_stock_report(catalogue, threshold=20):
    """Print products at or below the stock threshold, sorted by stock level."""
    # 👉 YOUR CODE HERE
    low_items = [
        (sku, product) for sku, product in catalogue.items()
        if product["stock"] <= threshold
    ]
    low_items.sort(key=lambda x: x[1]["stock"])
    
    print(f"\n--- Low Stock Report (threshold: {threshold} units) ---")
    if not low_items:
        print("All products adequately stocked.")
        return
    for sku, product in low_items:
        print(f"")


# -----------------------------------------------------------------------------
# Run the required sequence
# -----------------------------------------------------------------------------

display_catalogue(catalogue)
search_by_tag(catalogue, "home office")
add_review(catalogue, "SKU-003", 5)
add_review(catalogue, "SKU-999", 4)
add_review(catalogue, "SKU-001", 7)
apply_category_discount(catalogue, "Peripherals", 10)
display_catalogue(catalogue)
low_stock_report(catalogue)
