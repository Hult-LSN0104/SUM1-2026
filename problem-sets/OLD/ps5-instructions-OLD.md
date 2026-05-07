# Problem Set 5 — Product Catalogue Manager
**LSN-0104 | Due: Before Session 11**
**Weight: 6% of final grade**

---

## Overview

You've learned lists, tuples, and dictionaries. This problem set puts all three to work in a product catalogue system — the kind of data structure that sits at the core of any e-commerce or inventory application.

---

## Data Structure

Your catalogue will use a **dictionary of dictionaries**. Each key is a SKU (string), and each value is a dictionary with product details:

```python
catalogue = {
    "SKU-001": {
        "name": "Laptop Stand",
        "category": "Accessories",
        "price": 29.99,
        "tags": ("ergonomic", "home office", "adjustable"),
        "stock": 45,
        "reviews": [4, 5, 3, 5, 4]
    },
    ...
}
```

Note: `tags` is a **tuple** (immutable — tags don't change once set).
`reviews` is a **list** (mutable — new reviews get added over time).

---

## Starting Data

```python
catalogue = {
    "SKU-001": {"name": "Laptop Stand",       "category": "Accessories", "price": 29.99, "tags": ("ergonomic", "home office", "adjustable"), "stock": 45, "reviews": [4, 5, 3, 5, 4]},
    "SKU-002": {"name": "Wireless Mouse",      "category": "Peripherals", "price": 19.99, "tags": ("wireless", "compact", "home office"),     "stock": 120,"reviews": [3, 4, 4, 5, 3, 4]},
    "SKU-003": {"name": "USB-C Hub",           "category": "Peripherals", "price": 49.99, "tags": ("connectivity", "multi-port", "usb-c"),    "stock": 33, "reviews": [5, 5, 4, 4, 5]},
    "SKU-004": {"name": "Webcam HD",           "category": "Peripherals", "price": 79.99, "tags": ("video", "hd", "streaming"),               "stock": 18, "reviews": [4, 3, 4, 5]},
    "SKU-005": {"name": "Desk Lamp",           "category": "Furniture",   "price": 34.99, "tags": ("lighting", "adjustable", "home office"),  "stock": 62, "reviews": [4, 4, 5, 3, 4, 5]},
    "SKU-006": {"name": "Mechanical Keyboard", "category": "Peripherals", "price": 89.99, "tags": ("mechanical", "tactile", "rgb"),           "stock": 27, "reviews": [5, 5, 5, 4, 5]},
}
```

---

## Requirements

Write the following **five functions**:

### 1. `display_catalogue(catalogue)`
Print all products in a formatted table showing SKU, name, category, price, stock, and average review score (rounded to 1 decimal place).

### 2. `search_by_tag(catalogue, tag)`
Return a list of SKUs for products whose `tags` tuple contains the given tag (case-insensitive). Print the matching products or "No results found."

### 3. `add_review(catalogue, sku, rating)`
Add a rating (integer 1–5) to a product's reviews list. Validate that the SKU exists and the rating is between 1 and 5. Print a confirmation.

### 4. `apply_category_discount(catalogue, category, discount_percent)`
Apply a percentage discount to all products in a given category. Update the prices in the catalogue and print a summary of what changed.

### 5. `low_stock_report(catalogue, threshold=20)`
Print a report of all products at or below the threshold, sorted by stock level (lowest first).

---

## After writing your functions, run this sequence:

```python
display_catalogue(catalogue)
search_by_tag(catalogue, "home office")
add_review(catalogue, "SKU-003", 5)
add_review(catalogue, "SKU-999", 4)      # should handle missing SKU gracefully
add_review(catalogue, "SKU-001", 7)      # should handle invalid rating gracefully
apply_category_discount(catalogue, "Peripherals", 10)
display_catalogue(catalogue)             # prices should have changed
low_stock_report(catalogue)
```

---

## Stretch Goals *(optional)*

- Add a `add_product` function that lets the user add a new product interactively.
- Add a `sort_by` parameter to `display_catalogue` that accepts `"price"`, `"stock"`, or `"rating"`.

---

## Submission

Upload your completed `starter.py` to Canvas by the deadline.

---

## Grading

| Criterion | Marks |
|-----------|-------|
| Program runs without errors | 1 |
| `display_catalogue` shows all fields including avg rating | 2 |
| `search_by_tag` returns correct results | 2 |
| `add_review` validates input and updates correctly | 2 |
| `apply_category_discount` updates prices correctly | 2 |
| `low_stock_report` sorted correctly | 1 |
| **Total** | **10** |
