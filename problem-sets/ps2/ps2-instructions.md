# Problem Set 2 — Control Structures & Functions

**LSN-0104 | Covers Sessions 5–8 | Due: End of Week 4**

---

## Submission Instructions

- Submit a single Python file named `ps2_<your_last_name>.py` via the course portal.
- All code must run without errors. Test edge cases before submitting.
- Use docstrings for every function you define.
- Academic integrity: all code must be your own.
- Per Hult policy, assignments will be open for a maximum of 48 hours after the due date.
- Late submissions: After 48 hours beyond due date and time, any non-submitted assignments receive a grade of '0'.

---

## Exercise 1 — Tiered Discount Engine (20 pts)

Write a function called `get_discount(order_total)` that returns a discount rate based on this business logic:

```
$0 – $99.99      →  0%  (no discount)
$100 – $499.99   →  5%
$500 – $999.99   →  10%
$1,000+          →  20%
```

Then write a second function `apply_discount(order_total)` that:

- Calls `get_discount()` to retrieve the rate
- Calculates and returns the final price after the discount
- Prints a message like: `'$750.00 order qualifies for a 10% discount. Final price: $675.00'`

Test your functions with at least 4 different order totals that cover each tier.

---

## Exercise 2 — Loan Eligibility System (20 pts)

Build a loan eligibility checker function called `check_loan(income, credit_score, loan_amount)`. The logic:

- If `income < 30,000` → `'Ineligible: income below minimum threshold'`
- If `credit_score < 580` → `'Ineligible: credit score too low'`
- If `income >= 80,000` and `credit_score >= 750` → `'Approved: Premium rate (4.5%)'`
- If `income >= 50,000` and `credit_score >= 650` → `'Approved: Standard rate (6.5%)'`
- Otherwise → `'Approved: Higher risk rate (9.9%)'`

For approved loans, also calculate and print the estimated monthly payment using this simplified formula:

```
monthly = (loan_amount * rate) / 12
```

where `rate` is the annual interest rate as a decimal.

Wrap your function in a `try/except` block that catches `ValueError` if non-numeric values are entered. Test with at least 5 scenarios.

---

## Exercise 3 — Sales Report Generator (20 pts)

Given this dataset (hard-code it):

```python
reps  = ['Alice', 'Bob', 'Carol', 'David', 'Eva']
sales = [12400, 8300, 15600, 6700, 9800]
```

Write a program that:

- Uses a `for` loop with `enumerate()` to print each rep's name and sales figure
- Prints `'Top performer'` next to the rep with the highest sales
- Calculates and prints total, average, highest, and lowest sales
- Prints a simple text-based bar chart — each $1,000 in sales = one `█` character

Use at least two separate functions: one to compute statistics, one to print the report.

---

## Submission

Upload your completed `ps2_<your_last_name>.py` to the course portal by the deadline.

---

## Grading

**Total: 60 points**

| Criterion | Points |
| --- | --- |
| Exercise 1: Correct conditional logic in both functions, accurate discount calculation | 20 |
| Exercise 2: Multi-condition logic, correct rate application, `try/except` | 20 |
| Exercise 3: Loop with `enumerate`, statistics calculation, bar chart output | 20 |
| Code quality: docstrings on all functions, meaningful variable names | Checked |
| **Total** | **60** |
