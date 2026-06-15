# Problem Set 3 — Solution Guide
**LSN-0104 | Data Collections & File Handling**

> This is the most substantial problem set. Read through the full solution before reviewing your own work — pay close attention to the comments explaining *why* each design decision was made, not just *what* the code does.

---

## Sample CSV — `sales_data.csv`

Before running Exercise 3 you need a file in the same folder as your script. Create it with exactly these contents:

```
date,rep_name,product,quantity,unit_price,region
2026-04-01,Alice,Widget Pro,10,19.99,North
2026-04-01,Alice,Gadget Plus,5,49.99,North
2026-04-02,Bob,Widget Pro,8,19.99,South
2026-04-02,Bob,Thingamajig,20,4.99,South
2026-04-03,Carol,Gadget Plus,7,49.99,West
2026-04-03,Carol,Widget Pro,12,19.99,West
2026-04-04,Alice,Thingamajig,30,4.99,North
2026-04-05,Bob,Gadget Plus,4,49.99,South
2026-04-06,Carol,Thingamajig,25,4.99,West
2026-04-07,Alice,Gadget Plus,8,49.99,North
2026-04-08,Bob,Widget Pro,6,19.99,South
2026-04-09,Carol,Widget Pro,9,19.99,West
2026-04-10,Alice,Widget Pro,7,19.99,North
2026-04-11,Bob,Thingamajig,15,4.99,South
2026-04-12,Carol,Gadget Plus,6,49.99,West
```

---

## Exercise 1 — Inventory Manager (15 pts)

### Solution

```python
import csv
from datetime import datetime

inventory = [
    {"name": "Widget Pro",  "sku": "WP-001", "quantity": 25, "unit_price": 19.99},
    {"name": "Gadget Plus", "sku": "GP-002", "quantity": 10, "unit_price": 49.99},
    {"name": "Thingamajig","sku": "TJ-003", "quantity": 50, "unit_price":  4.99},
]


def view_items(items):
    """Print every item in the inventory in a readable table format."""
    if not items:
        print("  (no items in inventory)")
        return
    print(f"  {'SKU':<10} {'Name':<16} {'Qty':>5}  {'Unit Price':>10}  {'Value':>10}")
    print("  " + "-" * 56)
    for item in items:
        value = item["quantity"] * item["unit_price"]
        print(f"  {item['sku']:<10} {item['name']:<16} {item['quantity']:>5}  "
              f"${item['unit_price']:>9.2f}  ${value:>9.2f}")


def add_item(items):
    """Prompt the user for name, sku, quantity, unit_price; append to items."""
    name  = input("  Item name: ").strip()
    sku   = input("  SKU: ").strip()
    try:
        qty   = int(input("  Quantity: "))
        price = float(input("  Unit price: "))
    except ValueError:
        print("  Invalid quantity or price — item not added.")
        return
    items.append({"name": name, "sku": sku, "quantity": qty, "unit_price": price})
    print(f"  '{name}' added.")


def remove_item(items, sku):
    """Remove the item with the given SKU. Print a message if not found."""
    for item in items:
        if item["sku"] == sku:
            items.remove(item)
            print(f"  SKU {sku} removed.")
            return
    print(f"  SKU '{sku}' not found.")


def update_quantity(items, sku, new_quantity):
    """Update the quantity for the item with the given SKU."""
    for item in items:
        if item["sku"] == sku:
            item["quantity"] = new_quantity
            print(f"  {item['name']} quantity updated to {new_quantity}.")
            return
    print(f"  SKU '{sku}' not found.")


def total_value(items):
    """Return the sum of (quantity * unit_price) across all items."""
    return sum(i["quantity"] * i["unit_price"] for i in items)


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

        if choice == "1":
            view_items(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            sku = input("  Enter SKU to remove: ").strip()
            remove_item(inventory, sku)
        elif choice == "4":
            sku = input("  Enter SKU to update: ").strip()
            try:
                qty = int(input("  New quantity: "))
                update_quantity(inventory, sku, qty)
            except ValueError:
                print("  Quantity must be a whole number.")
        elif choice == "5":
            print(f"  Total inventory value: ${total_value(inventory):,.2f}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice — please enter 1–6.")
```

### Expected Output (view all items)
```
  SKU        Name              Qty   Unit Price       Value
  --------------------------------------------------------
  WP-001     Widget Pro         25      $19.99      $499.75
  GP-002     Gadget Plus        10      $49.99      $499.90
  TJ-003     Thingamajig        50       $4.99      $249.50
```

### Key Concepts

| Concept | Explanation |
|---|---|
| List of dicts | Each inventory item is a `dict`; all items live in a `list` — this is the standard pattern for tabular in-memory data |
| Looping with `for item in items` | Iterates over each dict in the list — no index needed unless you're removing while iterating (dangerous) |
| `items.remove(item)` | Removes by object reference after you've already found the matching item — safer than removing by index |
| `try/except` in `add_item` | Wraps `int()` and `float()` conversions so bad input doesn't crash the menu |
| `while True` / `break` | The menu runs forever until the user explicitly picks Exit — the only way out is the `break` |
| `else` catch-all | The final `else` in the menu dispatcher handles anything that isn't `1–6`, printing a friendly message instead of crashing |

> **Why not use `items.pop(i)` to remove?** You could find the index with `enumerate()` and call `pop()`, but `list.remove(item)` is cleaner when you already have a reference to the object. Just be careful: never call `list.remove()` *while* you're iterating over that list — always `return` immediately after removing.

---

## Exercise 2 — Customer Profile Manager (15 pts)

### Solution

```python
customers = {
    "C001": {"name": "Alice Johnson", "email": "alice@example.com", "tier": "Silver",
             "purchases": [120.00, 89.50, 240.75]},
    "C002": {"name": "Bob Smith",     "email": "bob@example.com",   "tier": "Bronze",
             "purchases": [49.99, 19.99]},
    "C003": {"name": "Carol White",   "email": "carol@example.com", "tier": "Silver",
             "purchases": [1500.00, 2200.00, 1800.00, 600.00]},
    "C004": {"name": "David Lee",     "email": "david@example.com", "tier": "Bronze",
             "purchases": [75.00, 150.00, 95.50]},
}


def summarize_customers(customers):
    """Print a summary for each customer: name, email, tier, total spent, average purchase."""
    print(f"\n{'ID':<6} {'Name':<16} {'Email':<26} {'Tier':<8} {'Total':>9}  {'Avg':>8}")
    print("-" * 78)
    for cid, data in customers.items():   # .items() gives (key, value) pairs
        total = sum(data["purchases"])
        avg   = total / len(data["purchases"])
        print(f"{cid:<6} {data['name']:<16} {data['email']:<26} "
              f"{data['tier']:<8} ${total:>8.2f}  ${avg:>7.2f}")


def find_top_customer(customers):
    """Return the customer ID of the customer with the highest total spending."""
    # max() over the keys, using total purchases as the sort key
    # .values() used inside the lambda to access each customer's data
    return max(customers, key=lambda cid: sum(customers[cid]["purchases"]))


def upgrade_to_gold(customers):
    """Upgrade any customer with total spending > $5,000 to 'Gold' tier."""
    for cid in customers.keys():   # .keys() iterates over customer IDs
        total = sum(customers[cid]["purchases"])
        if total > 5_000:
            customers[cid]["tier"] = "Gold"
            print(f"  {customers[cid]['name']} upgraded to Gold (total: ${total:,.2f})")
```

### Expected Output
```
ID     Name             Email                      Tier         Total       Avg
------------------------------------------------------------------------------
C001   Alice Johnson    alice@example.com          Silver   $  450.25  $ 150.08
C002   Bob Smith        bob@example.com            Bronze   $   69.98  $  34.99
C003   Carol White      carol@example.com          Silver   $ 6100.00  $1525.00
C004   David Lee        david@example.com          Bronze   $  320.50  $ 106.83

Top customer: C003 — Carol White
  Carol White upgraded to Gold (total: $6,100.00)

After tier upgrades:
ID     Name             Email                      Tier         Total       Avg
------------------------------------------------------------------------------
C001   Alice Johnson    alice@example.com          Silver   $  450.25  $ 150.08
C002   Bob Smith        bob@example.com            Bronze   $   69.98  $  34.99
C003   Carol White      carol@example.com          Gold     $ 6100.00  $1525.00
C004   David Lee        david@example.com          Bronze   $  320.50  $ 106.83
```

### Key Concepts

| Concept | Explanation |
|---|---|
| Nested dict | The outer dict maps `customer_id → profile_dict`. The inner dict holds all fields including `purchases` (a list) |
| `.items()` | Returns `(key, value)` pairs — the most common way to loop a dict when you need both |
| `.keys()` | Returns just the keys — used in `upgrade_to_gold` to iterate IDs while modifying values |
| `.values()` | Would return just the profile dicts — useful when you don't need the ID |
| `max(dict, key=...)` | `max()` over a dict iterates its keys by default; the `key=` lambda tells it what to measure |
| Lambda | `lambda cid: sum(customers[cid]["purchases"])` is an inline function — equivalent to writing a named helper just for this one comparison |
| Mutating inside a loop | In `upgrade_to_gold`, we change `customers[cid]["tier"]` while looping — this is safe because we're modifying a *value*, not the structure of the dict being iterated |

> **`.items()` vs `.keys()` vs `.values()` — when to use which?**
> - Need both key and value → `.items()` (most common)
> - Need only keys (e.g. to look up values separately) → `.keys()` or just `for k in dict`
> - Need only values (e.g. to sum or compare) → `.values()`

---

## Exercise 3 — CSV Sales Processor (30 pts)

### Part A — Read and Parse

```python
def load_sales(path):
    """Read the CSV, convert types, add a revenue field, return list of dicts."""
    records = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)      # Each row becomes a dict keyed by header
        for row in reader:
            row["quantity"]   = int(row["quantity"])
            row["unit_price"] = float(row["unit_price"])
            row["revenue"]    = row["quantity"] * row["unit_price"]  # Derived field
            records.append(row)
    return records
```

### Part B — Analyze

```python
def analyze_sales(records):
    """Compute totals, averages, top rep, regional breakdown, and best product."""
    total_revenue   = sum(r["revenue"] for r in records)
    average_revenue = total_revenue / len(records)

    # Accumulate revenue per rep using .get() with a default of 0
    rep_totals = {}
    for r in records:
        rep_totals[r["rep_name"]] = rep_totals.get(r["rep_name"], 0) + r["revenue"]
    top_rep_name = max(rep_totals, key=rep_totals.get)

    # Revenue by region — same accumulation pattern
    revenue_by_region = {}
    for r in records:
        revenue_by_region[r["region"]] = revenue_by_region.get(r["region"], 0) + r["revenue"]

    # Units sold by product
    product_units = {}
    for r in records:
        product_units[r["product"]] = product_units.get(r["product"], 0) + r["quantity"]
    best_product_name = max(product_units, key=product_units.get)

    return {
        "total_revenue":     total_revenue,
        "average_revenue":   average_revenue,
        "top_rep":           {"name": top_rep_name, "revenue": rep_totals[top_rep_name]},
        "revenue_by_region": revenue_by_region,
        "best_product":      {"name": best_product_name, "units_sold": product_units[best_product_name]},
    }
```

### Part C — Write Report

```python
def write_report(stats, path):
    """Write a formatted human-readable report to path."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append("=" * 40)
    lines.append("   SALES PERFORMANCE REPORT")
    lines.append(f"   Generated: {now}")
    lines.append("=" * 40)
    lines.append("")
    lines.append("OVERALL SUMMARY")
    lines.append(f"  Total Records:   {stats['record_count']}")
    lines.append(f"  Total Revenue:   ${stats['total_revenue']:,.2f}")
    lines.append(f"  Average Sale:    ${stats['average_revenue']:,.2f}")
    lines.append("")
    lines.append("REGIONAL BREAKDOWN")
    for region, rev in sorted(stats["revenue_by_region"].items()):
        lines.append(f"  {region:<8} ${rev:,.2f}")
    lines.append("")
    lines.append(f"TOP PERFORMER:  {stats['top_rep']['name']} — ${stats['top_rep']['revenue']:,.2f}")
    lines.append(f"BEST PRODUCT:   {stats['best_product']['name']} ({stats['best_product']['units_sold']} units sold)")
    lines.append("")
    lines.append("=" * 40)

    with open(path, "w") as f:
        f.write("\n".join(lines))
```

### Expected Report Output (`sales_report.txt`)
```
========================================
   SALES PERFORMANCE REPORT
   Generated: 2026-04-12 09:00
========================================

OVERALL SUMMARY
  Total Records:   15
  Total Revenue:   $2,988.28
  Average Sale:    $199.22

REGIONAL BREAKDOWN
  North    $1,139.40
  South    $654.47
  West     $1,194.41

TOP PERFORMER:  Carol — $1,194.41
BEST PRODUCT:   Thingamajig (90 units sold)

========================================
```

### Main block

```python
if __name__ == "__main__":
    # ---- Exercise 2 ----
    summarize_customers(customers)
    top_id = find_top_customer(customers)
    print(f"\nTop customer: {top_id} — {customers[top_id]['name']}")
    upgrade_to_gold(customers)
    print("\nAfter tier upgrades:")
    summarize_customers(customers)

    # ---- Exercise 3 ----
    records = load_sales(CSV_PATH)
    print(f"\nLoaded {len(records)} records")
    stats = analyze_sales(records)
    stats["record_count"] = len(records)
    write_report(stats, REPORT_PATH)
    print(f"Report written to {REPORT_PATH}")
```

### Key Concepts — Exercise 3

| Concept | Explanation |
|---|---|
| `csv.DictReader` | Reads the header row automatically and turns each subsequent row into a dict — much cleaner than `csv.reader` for named columns |
| `newline=""` in `open()` | Required by the `csv` module on Windows to prevent extra blank lines being inserted |
| Type conversion on load | CSV files store everything as strings — always convert `quantity` to `int` and `unit_price` to `float` immediately after reading, before doing any math |
| `dict.get(key, 0)` | Returns `0` if the key doesn't exist yet — the standard way to accumulate counts or totals into a dict without a `KeyError` |
| `max(dict, key=dict.get)` | Finds the key with the largest value — equivalent to `max(d, key=lambda k: d[k])` but more concise |
| `open(path, "w")` | Opens a file for writing — creates it if it doesn't exist, overwrites if it does |
| `"\n".join(lines)` | Builds the full report string from a list of lines — cleaner than calling `f.write()` on every line individually |
| `datetime.now().strftime(...)` | Formats the current date/time as a readable string for the report header |

---

## Putting It All Together — `if __name__ == "__main__"`

You'll notice the starter file wraps all function calls in `if __name__ == "__main__":`. This is a Python best practice:

```python
if __name__ == "__main__":
    # This code only runs when you execute the file directly
    # It does NOT run if another script imports your functions
    inventory_menu()
```

Without this guard, importing any function from your file would accidentally trigger the whole menu loop or print output. With it, your functions are safely reusable as a module.

---

## Quick Reference — New Concepts in PS3

| Concept | Syntax | Notes |
|---|---|---|
| List of dicts | `[{"key": val}, ...]` | Standard pattern for tabular in-memory data |
| Nested dict | `{"id": {"field": val}}` | Outer key is the ID; inner dict holds all fields |
| `.items()` | `for k, v in d.items()` | Key + value pairs — most common dict loop |
| `.keys()` | `for k in d.keys()` | Keys only (same as `for k in d`) |
| `.values()` | `for v in d.values()` | Values only |
| `dict.get(k, default)` | `d.get("key", 0)` | Safe lookup — returns default instead of crashing |
| `csv.DictReader` | `reader = csv.DictReader(f)` | Turns each CSV row into a dict |
| File write | `with open(path, "w") as f:` | Creates or overwrites a file |
| `datetime.now()` | `datetime.now().strftime("%Y-%m-%d")` | Current timestamp as a formatted string |
| `if __name__ == "__main__"` | Guard block at bottom of file | Prevents code from running on import |
