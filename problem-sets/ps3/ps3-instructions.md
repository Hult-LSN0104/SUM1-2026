# Problem Set 3 — Data Collections & File Handling

**LSN-0104 | Covers Sessions 9–12 | Due: End of Week 6**

---

## Submission Instructions

- Submit your Python file(s) AND any output files as a `.zip` named `ps3_<your_last_name>.zip`.
- All code must run without errors. Include your sample CSV file in the zip.
- Use docstrings and comments throughout.
- This is the most substantial problem set — start early.
- Late submissions: -10% per day.

---

## Exercise 1 — Inventory Manager (15 pts)

Build a command-line inventory manager using a list of dictionaries. Each item should have: `name`, `sku`, `quantity`, and `unit_price`. The program should present a menu loop:

```
===== INVENTORY MANAGER =====
1. View all items
2. Add new item
3. Remove item by SKU
4. Update quantity by SKU
5. Show total inventory value
6. Exit
```

**Requirements:**

- Use a list of dictionaries as the data structure
- Start with at least 3 pre-loaded items
- Total inventory value = sum of (`quantity × unit_price`) for all items
- Use `while True` with `break` to keep the menu running until the user exits
- Handle invalid menu entries gracefully (no crashes)

---

## Exercise 2 — Customer Profile Manager (15 pts)

Build a dictionary-based customer profile system. Use a nested dictionary where the outer key is the customer ID (e.g., `'C001'`) and the value is a dict with: `name`, `email`, `tier`, and `purchases` (a list of amounts).

Your program should:

- Hard-code at least 4 customers with 2–5 purchase amounts each
- Print a summary for each customer: name, email, tier, total spent, and average purchase
- Find and print the highest-value customer (most total spending)
- Upgrade any customer with total spending > $5,000 to `'Gold'` tier
- Use `.items()`, `.values()`, and `.keys()` at least once each

---

## Exercise 3 — CSV Sales Processor (30 pts)

This is the capstone exercise. You will be provided with (or create) a CSV file called `sales_data.csv` with these columns:

```
date,rep_name,product,quantity,unit_price,region
```

Create a sample CSV with at least 15 rows of realistic data across 3 regions and 3 sales reps. Then write a program that:

### Part A — Read and Parse (10 pts)

- Opens and reads `sales_data.csv` using the `csv` module
- Stores each row as a dictionary in a list
- Calculates revenue (`quantity × unit_price`) for each row
- Prints the total number of records loaded

### Part B — Analyze (10 pts)

- Calculates total and average revenue across all transactions
- Identifies the top sales rep (by total revenue)
- Calculates total revenue by region
- Finds the best-selling product by total quantity

### Part C — Write Report (10 pts)

- Writes a formatted summary report to a new file: `sales_report.txt`
- The report should include: overall totals, per-region breakdown, top rep, best product
- The report must be human-readable — use section headers and alignment

**Sample report structure:**

```
================================
   SALES PERFORMANCE REPORT
   Generated: [date]
================================

OVERALL SUMMARY
  Total Records:   15
  Total Revenue:   $48,320.00
  Average Sale:    $3,221.33

REGIONAL BREAKDOWN
  North:  $18,400.00
  South:  $15,200.00
  West:   $14,720.00

TOP PERFORMER:  Alice — $21,000.00
BEST PRODUCT:   Widget Pro (47 units sold)
```

---

## Submission

Upload your completed `ps3_<your_last_name>.zip` (containing your Python file(s), the sample CSV, and the generated report) to the course portal by the deadline.

---

## Grading

**Total: 60 points**

| Criterion | Points |
| --- | --- |
| Exercise 1: Menu loop, list of dicts, CRUD operations, inventory value | 15 |
| Exercise 2: Nested dicts, correct aggregation, tier upgrade logic | 15 |
| Exercise 3A: CSV reading, row parsing, revenue calculation | 10 |
| Exercise 3B: Correct analytics — totals, top rep, regional, best product | 10 |
| Exercise 3C: Formatted text report written to file, human-readable | 10 |
| Code quality: functions, docstrings, comments, error handling | Checked |
| **Total** | **60** |
