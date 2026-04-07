# Capstone Project — Customer Sales Report Generator
**LSN-0104 | Due: Session 12 (presented in class)**
**Weight: 40% of final grade**

---

## Overview

This is your final project. You'll build a complete, end-to-end Python program that loads real transaction data, processes it using everything you've learned, and produces a professional report — the kind of output a business analyst or operations team would actually use.

This is not a problem set with step-by-step instructions. It's an open brief. You decide how to structure your code, what your report looks like, and how far you push it.

---

## The Scenario

You work as a junior data analyst at **Northbridge Solutions**, a B2B office supplies company. Your manager has asked you to write a Python script that processes the company's customer transaction data and produces two outputs:

1. A formatted **text report** (`customer_report.txt`) summarising each customer's activity
2. A **CSV summary file** (`customer_summary.csv`) that can be opened in Excel

The transaction data is in `transactions.csv` in this folder.

---

## Minimum Requirements

Your program must do all of the following to pass.

### Data Loading
- Read `transactions.csv` using Python's `csv` module
- Handle the case where the file is missing (use `try/except`)

### Processing
- Calculate each customer's **total spend** across all transactions
- Calculate each customer's **transaction count**
- Identify each customer's **most purchased product** (by quantity)
- Assign each customer a **loyalty tier** based on total spend:

| Total Spend | Tier |
|-------------|------|
| $5,000 or more | Platinum |
| $2,000–$4,999 | Gold |
| $500–$1,999 | Standard |
| Under $500 | New |

- Apply a **loyalty discount** to each customer's spend:

| Tier | Discount |
|------|----------|
| Platinum | 15% |
| Gold | 10% |
| Standard | 5% |
| New | 0% |

### Output — Text Report (`customer_report.txt`)
- Report title and generation date/time
- One section per customer including: name, ID, tier, transaction count, total spend, discount applied, final spend after discount, most purchased product
- A grand totals section: total customers, total transactions, total revenue (pre and post discount)
- Customers sorted by total spend, highest first

### Output — Summary CSV (`customer_summary.csv`)
- One row per customer
- Columns: `customer_id`, `customer_name`, `tier`, `transaction_count`, `total_spend`, `discount_rate`, `final_spend`

### Code Quality
- All processing logic must be in **named functions** with docstrings
- No hardcoded magic numbers — use constants at the top of the file
- Your code must run without errors from top to bottom

---

## Presentation (Session 12)

You'll do a **5-minute demo** in class showing:
1. Running the program
2. Opening and walking through `customer_report.txt`
3. One thing you found interesting or difficult

There are no slides required. Just your terminal and your output file.

---

## Grading Rubric

| Criterion | Marks |
|-----------|-------|
| Program runs without errors end to end | 10 |
| Data loaded correctly with error handling | 5 |
| All processing logic correct (totals, tiers, discounts, top product) | 15 |
| Text report is complete, formatted, and includes grand totals | 15 |
| Summary CSV is correctly structured and readable | 10 |
| Functions used throughout with docstrings | 10 |
| Constants used instead of hardcoded values | 5 |
| In-class demo — program runs live, output explained clearly | 20 |
| Code is readable: clear variable names, comments where helpful | 10 |
| **Total** | **100** |

---

## Stretch Goals *(optional — impress us)*

- Add a **monthly breakdown** section to the report: revenue by month across all customers
- Identify customers whose spend this year is lower than the same period last year — potential churn risk
- Add a **"Top Products"** section showing the five best-selling products by total revenue
- Make the report look beautiful — alignment, separators, consistent formatting throughout
- Share your program as a Google Colab notebook so a classmate can run it with one click

---

## Files in This Folder

| File | Description |
|------|-------------|
| `transactions.csv` | Input data — 65 transactions across 12 customers |
| `starter.py` | Skeleton code with function signatures to get you started |
| `instructions.md` | This file |

---

## A Note on Using AI Tools

You may use Claude, GitHub Copilot, or other AI tools to help you understand errors, look up syntax, or explore ideas. You may not use them to generate your complete solution.

A good test: can you explain every line of your code out loud? If yes, it's yours. If not, go back and understand it before submitting.

---

*Good luck. You've built an invoice calculator, a loan checker, an inventory manager, and a customer profile system. This is the same thing — just bigger, and all at once.*
