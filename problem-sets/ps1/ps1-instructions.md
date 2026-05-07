# Problem Set 1 — Variables, Data Types & Strings

**LSN-0104 | Covers Sessions 1–4 | Due: End of Week 2**

---

## Submission Instructions

- Submit a single Python file named `ps1_<your_last_name>.py` via the course portal.
- All code must run without errors in Python 3.x. Test before submitting.
- Use comments to clearly label each exercise (e.g., `# Exercise 1`).
- Academic integrity: all code must be your own. Collaboration is encouraged for concepts, not code.
- Late submissions: -10% per day. Contact the instructor in advance for extensions.

---

## Exercise 1 — Hello, Business World! (10 pts)

Write a program that:

- Asks the user for their first name, last name, and company name using `input()`
- Prints a professional greeting: `Hello, [First] [Last] from [Company]! Welcome to Python.`
- Prints the full name in ALL CAPS and the company name in Title Case on separate lines
- Prints the total number of characters in the full name (including the space)

**Expected output example** (for input: `Maria` / `Garcia` / `globex industries`):

```
Hello, Maria Garcia from Globex Industries! Welcome to Python.
Full name (uppercase): MARIA GARCIA
Company (title case): Globex Industries
Name length: 12 characters
```

---

## Exercise 2 — Invoice Calculator (20 pts)

Build an interactive invoice calculator that:

- Asks the user for: product name, unit price (`float`), and quantity (`int`)
- Calculates: `subtotal = price × quantity`
- Applies an 8% sales tax to get the total
- Prints a formatted invoice summary with:
    - Product name, unit price, quantity, subtotal, tax amount, and total
    - All currency values displayed with a `$` sign and 2 decimal places
- Uses at least one f-string

**Expected output example** (product: `Widget Pro`, price: `24.99`, qty: `5`):

```
===== INVOICE =====
Product:     Widget Pro
Unit Price:  $24.99
Quantity:    5
Subtotal:    $124.95
Tax (8%):    $9.996
Total Due:   $134.95
===================
```

---

## Exercise 3 — Customer Data Cleaner (20 pts)

A company receives customer data that is inconsistently formatted. Given this messy data (hard-code it in your program):

```python
raw_name  = '  jANe  dOe  '
raw_email = '  Jane.Doe@COMPANY.COM  '
raw_phone = '(617) 555-0142'
```

Your program should:

- Strip whitespace from name and email
- Convert name to Title Case and email to lowercase
- Check if the email ends with `'@company.com'` — print `'Internal employee'` or `'External contact'`
- Extract the area code from the phone number (first 3 digits inside the parentheses)
- Print a clean formatted customer card showing all cleaned values and findings

---

## Exercise 4 — Profit Margin Calculator (10 pts)

Build a program that:

- Asks the user for revenue and cost of goods sold (COGS)
- Calculates gross profit (`revenue – COGS`) and gross margin % (`(gross profit / revenue) × 100`)
- Uses the `math` module to also print the ceiling and floor of the margin percentage
- Formats output with 2 decimal places and a `%` symbol

**Bonus (+5 pts):** use `round()` to also display a rounded margin and explain in a comment when rounding vs. truncating matters in finance.

---

## Submission

Upload your completed `ps1_<your_last_name>.py` to the course portal by the deadline.

---

## Grading

**Total: 60 points + 5 bonus**

| Criterion | Points |
| --- | --- |
| Exercise 1: Correct use of `input()`, string methods, and `len()` | 10 |
| Exercise 2: Correct calculations, formatting, and f-strings | 20 |
| Exercise 3: String cleaning, conditional logic, and formatted output | 20 |
| Exercise 4: Arithmetic, `math` module, and percentage formatting | 10 |
| Code quality: clear comments, descriptive variable names, readable structure | 5 (bonus) |
| **Total** | **60 + 5 bonus** |