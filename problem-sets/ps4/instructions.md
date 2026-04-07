# Problem Set 4 — Payroll Calculator
**LSN-0104 | Due: Before Session 9**
**Weight: 6% of final grade**

---

## Overview

You've learned how to write functions and handle errors. This problem set asks you to build a modular payroll calculator — a real-world use case where clean, reusable functions matter.

---

## Payroll Rules

**Gross pay:**
- Regular hours (up to 40/week): paid at the base hourly rate
- Overtime hours (anything over 40): paid at 1.5× the base rate

**Deductions (applied to gross pay):**
- Federal tax: 22%
- State tax: 5%
- Health insurance: $85.00 flat per pay period (only for full-time employees)

**Employee types:**
- `"full_time"` — eligible for health insurance deduction
- `"part_time"` — no health insurance deduction

**Net pay** = gross pay − federal tax − state tax − health insurance (if applicable)

---

## Requirements

Write the following **four functions**, then use them to process the employee list below.

### Function 1: `calculate_gross_pay(hours, rate)`
Takes hours worked and hourly rate. Returns gross pay including overtime.

### Function 2: `calculate_deductions(gross_pay, employee_type)`
Takes gross pay and employee type. Returns a dictionary:
```python
{"federal_tax": ..., "state_tax": ..., "health_insurance": ..., "total": ...}
```

### Function 3: `calculate_net_pay(gross_pay, deductions)`
Takes gross pay and the deductions dictionary. Returns net pay.

### Function 4: `print_pay_stub(employee, gross, deductions, net)`
Takes an employee dictionary, gross pay, deductions dict, and net pay.
Prints a formatted pay stub like this:

```
══════════════════════════════════════
  PAY STUB — Alice Johnson
  Role: Sales Manager | Full Time
══════════════════════════════════════
  Hours worked:      42.0
  Hourly rate:      $28.50
  Regular pay:    $1,140.00  (40 hrs)
  Overtime pay:      $85.50  (2 hrs @ 1.5x)
  Gross Pay:      $1,225.50
──────────────────────────────────────
  Federal Tax (22%): -$269.61
  State Tax (5%):     -$61.28
  Health Insurance:   -$85.00
  Total Deductions:  -$415.89
──────────────────────────────────────
  NET PAY:           $809.61
══════════════════════════════════════
```

---

## Employee Data

```python
employees = [
    {"name": "Alice Johnson",  "role": "Sales Manager",    "type": "full_time",  "hours": 42.0, "rate": 28.50},
    {"name": "Bob Smith",      "role": "Sales Rep",        "type": "full_time",  "hours": 40.0, "rate": 22.00},
    {"name": "Carol White",    "role": "Lead Developer",   "type": "full_time",  "hours": 45.5, "rate": 45.00},
    {"name": "David Lee",      "role": "Marketing Coord.", "type": "part_time",  "hours": 20.0, "rate": 18.00},
    {"name": "Elena Garcia",   "role": "Data Analyst",     "type": "full_time",  "hours": 38.0, "rate": 35.00},
    {"name": "Frank Nguyen",   "role": "Support Agent",    "type": "part_time",  "hours": 25.5, "rate": 16.50},
]
```

---

## Requirements (continued)

After processing all employees, print a **payroll summary** showing:
- Total gross payroll
- Total deductions
- Total net payroll
- Highest paid employee (by net pay)

---

## Error Handling

Add input validation to `calculate_gross_pay`:
- If `hours` is negative, raise a `ValueError` with a clear message.
- If `rate` is zero or negative, raise a `ValueError` with a clear message.
- Wrap your function calls in `try/except` blocks to handle these gracefully.

---

## Stretch Goals *(optional)*

- Add a `bonus_percent` parameter to `calculate_gross_pay` (default 0) that adds a percentage bonus to gross pay.
- Calculate and display each employee's effective tax rate (total tax / gross pay).

---

## Submission

Upload your completed `starter.py` to Canvas by the deadline.

---

## Grading

| Criterion | Marks |
|-----------|-------|
| Program runs without errors | 1 |
| `calculate_gross_pay` correctly handles regular and overtime | 2 |
| `calculate_deductions` returns correct values for both employee types | 2 |
| `calculate_net_pay` returns correct result | 1 |
| `print_pay_stub` produces clear, formatted output | 2 |
| Payroll summary printed at the end | 1 |
| Error handling with `try/except` | 1 |
| **Total** | **10** |
