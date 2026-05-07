# Problem Set 2 — Sales Data Cleaner & Formatter
**LSN-0104 | Due: Before Session 5**
**Weight: 6% of final grade**

---

## Overview

Raw data from business systems is almost never clean. In this problem set you'll write a program that takes messy sales records, cleans them up using string methods, performs calculations, and prints a formatted summary.

---

## The Data

Your program will work with the following list of raw sales records. Each record is a string in this format:

```
"rep name | product | quantity | unit price"
```

The data has real-world messiness: inconsistent capitalisation, extra spaces, and prices that include a `$` sign.

```python
raw_records = [
    "  alice johnson | laptop stand | 5 | $29.99  ",
    "BOB SMITH | wireless mouse | 12 | $19.99",
    "  Carol White  | usb-c hub | 3 | $49.99",
    "david lee|WEBCAM HD|7|$79.99",
    "ELENA GARCIA | desk lamp | 9 | $34.99  ",
    "  Alice Johnson | mechanical keyboard | 2 | $89.99",
    "bob smith | laptop stand | 8 | $29.99",
    "Carol White | NOISE-CANCELLING HEADPHONES | 1 | $129.99  ",
]
```

---

## Requirements

Your program must:

1. **Parse each record** — split each string into its four fields using `.split("|")`.

2. **Clean each field**:
   - Rep name: stripped of whitespace, in Title Case
   - Product: stripped, in Title Case
   - Quantity: stripped, converted to `int`
   - Unit price: stripped, `$` removed, converted to `float`

3. **Calculate the line total** for each record (quantity × unit price).

4. **Print a formatted table** of cleaned records:

```
Rep               Product                       Qty   Unit Price   Line Total
------------------------------------------------------------------------------
Alice Johnson     Laptop Stand                    5       $29.99     $149.95
Bob Smith         Wireless Mouse                 12       $19.99     $239.88
...
```

5. **Print a summary section** below the table showing:
   - Total records processed
   - Grand total revenue across all records
   - The rep with the highest combined sales

---

## Hints

- `"$29.99".replace("$", "")` → `"29.99"`
- `.split("|")` splits a string into a list at every `|`
- `parts[0].strip().title()` cleans index 0 of a split list
- For the summary, a dictionary keyed by rep name is a good approach (preview of Week 5!)

---

## Stretch Goals *(optional)*

- Sort the table by line total, highest first.
- Group the results by rep and print a per-rep subtotal.
- Flag any record where the line total exceeds $500.

---

## Submission

Upload your completed `starter.py` to Canvas by the deadline.

---

## Grading

| Criterion | Marks |
|-----------|-------|
| Program runs without errors | 2 |
| All four fields correctly parsed and cleaned | 3 |
| Line totals correctly calculated | 2 |
| Formatted table printed cleanly | 2 |
| Summary section with grand total and top rep | 1 |
| **Total** | **10** |
