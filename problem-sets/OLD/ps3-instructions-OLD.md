# Problem Set 3 — Shipping Cost Calculator
**LSN-0104 | Due: Before Session 7**
**Weight: 6% of final grade**

---

## Overview

You've learned conditionals and loops. Now apply them to a realistic business scenario: calculating shipping costs for a set of customer orders based on destination, weight, and service level.

---

## Shipping Rules

Use the following rules — these are the "business logic" your program must implement.

**Service levels and base rates (per kg):**

| Service | Domestic | International |
|---------|----------|---------------|
| Standard (5–7 days) | $0.80/kg | $2.50/kg |
| Express (2–3 days) | $1.50/kg | $4.00/kg |
| Overnight (next day) | $3.00/kg | Not available |

**Surcharges:**
- Orders under 1 kg are billed as 1 kg minimum
- Orders over 30 kg: add a $25.00 heavy item surcharge
- International orders: add a $15.00 customs handling fee
- Overnight is only available for domestic orders

**Free shipping:**
- Domestic orders over $200 in product value qualify for free Standard shipping
  (the customer still pays extra if they choose Express or Overnight)

---

## The Orders

```python
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
```

---

## Requirements

Your program must loop through `orders` and for each one:

1. **Apply the minimum weight rule** (treat anything under 1 kg as 1 kg).
2. **Check for invalid combinations** — if a customer requests Overnight for an international order, print a warning and bill them at the international Express rate instead.
3. **Calculate the shipping cost** based on service level and destination.
4. **Apply surcharges** where applicable.
5. **Apply free shipping** where applicable (only for the base Standard cost).
6. **Print one summary line per order**, for example:

```
ORD-101  Alice Johnson       domestic    standard    2.5kg   $  2.00  ✓ FREE (order > $200)
ORD-102  Bob Smith           intl        express     1.0kg   $ 19.15  (incl. customs $15.00)
ORD-103  Carol White         domestic    standard   35.0kg   $ 25.00  (heavy surcharge applied, FREE shipping)
```

7. **Print a totals section** at the end showing total shipping revenue collected.

---

## Hints

- Work through one order by hand on paper before writing any code.
- Use `if/elif/else` blocks for service level and destination.
- The free shipping rule only waives the base rate — surcharges still apply.

---

## Stretch Goals *(optional)*

- Count how many orders qualified for free shipping.
- Find the most expensive order to ship and print its details.
- Ask the user to enter a new order interactively and calculate its cost.

---

## Submission

Upload your completed `starter.py` to Canvas by the deadline.

---

## Grading

| Criterion | Marks |
|-----------|-------|
| Program runs without errors | 2 |
| Minimum weight and invalid combination rules applied | 2 |
| Shipping costs correctly calculated for all service/destination combinations | 3 |
| Surcharges correctly applied | 2 |
| Summary printed with totals | 1 |
| **Total** | **10** |
