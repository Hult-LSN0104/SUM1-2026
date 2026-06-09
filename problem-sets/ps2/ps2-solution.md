# Problem Set 2 — Solution Guide
**LSN-0104 | Control Structures & Functions**

> This guide walks through each exercise with the complete solution and explanation of key concepts. Read the comments carefully — they explain the *why*, not just the *what*.

---

## Exercise 1 — Tiered Discount Engine (20 pts)

### Solution

```python
def get_discount(order_total):
    """Return the discount rate (as a decimal) based on the order total.
    
    Args:
        order_total (float): The pre-discount order amount in dollars.
    
    Returns:
        float: Discount rate — 0.0, 0.05, 0.10, or 0.20.
    """
    if order_total >= 1000:
        return 0.20
    elif order_total >= 500:
        return 0.10
    elif order_total >= 100:
        return 0.05
    else:
        return 0.0


def apply_discount(order_total):
    """Apply the appropriate discount to an order and print a summary.
    
    Calls get_discount() to find the rate, calculates the final price,
    prints a formatted message, and returns the discounted total.
    
    Args:
        order_total (float): The pre-discount order amount in dollars.
    
    Returns:
        float: The final price after the discount is applied.
    """
    rate = get_discount(order_total)
    discount_amount = order_total * rate
    final_price = order_total - discount_amount

    # Convert rate to a clean percentage string for the message
    rate_pct = int(rate * 100)

    if rate_pct == 0:
        print(f"${order_total:.2f} order — no discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"${order_total:.2f} order qualifies for a {rate_pct}% discount. Final price: ${final_price:.2f}")

    return final_price


# --- Tests covering all four tiers ---
apply_discount(50)      # No discount
apply_discount(250)     # 5%
apply_discount(750)     # 10%
apply_discount(1200)    # 20%
```

### Expected Output
```
$50.00 order — no discount applied. Final price: $50.00
$250.00 order qualifies for a 5% discount. Final price: $237.50
$750.00 order qualifies for a 10% discount. Final price: $675.00
$1200.00 order qualifies for a 20% discount. Final price: $960.00
```

### Key Concepts

| Concept | Explanation |
|---|---|
| Chained `if/elif/else` | Each condition is checked in order — Python stops at the first `True` match |
| Check highest tier first | Starting with `>= 1000` means you don't need compound conditions like `500 <= x < 1000` |
| Separating concerns | `get_discount()` only calculates the rate; `apply_discount()` handles the rest — each function does one job |
| Docstrings | The triple-quoted string at the top of each function describes what it does, its arguments, and what it returns |

> **Why check highest tier first?** If you checked `>= 100` first, a $1,200 order would incorrectly get 5% — it would match the first `True` condition and stop. Always order `if/elif` from most specific (or highest) to least.

---

## Exercise 2 — Loan Eligibility System (20 pts)

### Solution

```python
def check_loan(income, credit_score, loan_amount):
    """Check loan eligibility and print the outcome with estimated monthly payment.

    Evaluates income and credit score against eligibility thresholds and
    assigns an interest rate tier. For approved loans, calculates and prints
    a simplified monthly payment estimate.

    Args:
        income (float): Annual income in dollars.
        credit_score (int): Applicant's credit score.
        loan_amount (float): Requested loan amount in dollars.

    Returns:
        str: An eligibility result message.
    """
    # --- Ineligibility checks first ---
    # Order matters: check hard disqualifiers before approval tiers
    if income < 30_000:
        result = "Ineligible: income below minimum threshold"
    elif credit_score < 580:
        result = "Ineligible: credit score too low"

    # --- Approval tiers (best to worst) ---
    elif income >= 80_000 and credit_score >= 750:
        result = "Approved: Premium rate (4.5%)"
        rate = 0.045
    elif income >= 50_000 and credit_score >= 650:
        result = "Approved: Standard rate (6.5%)"
        rate = 0.065
    else:
        result = "Approved: Higher risk rate (9.9%)"
        rate = 0.099

    print(result)

    # Only calculate a payment if the loan was approved
    if result.startswith("Approved"):
        monthly = (loan_amount * rate) / 12
        print(f"  → Estimated monthly payment: ${monthly:.2f}")

    return result


# --- Wrap calls in try/except to handle non-numeric input ---
def run_loan_check(income, credit_score, loan_amount):
    """Run check_loan with input validation via try/except.
    
    Args:
        income: Annual income — must be numeric.
        credit_score: Credit score — must be numeric.
        loan_amount: Loan amount — must be numeric.
    """
    try:
        check_loan(float(income), int(credit_score), float(loan_amount))
    except ValueError:
        print("Error: income, credit score, and loan amount must all be numbers.")
    print()  # Blank line between test cases


# --- Tests covering all 5 scenarios ---
run_loan_check(25_000, 700, 10_000)   # Ineligible: income too low
run_loan_check(45_000, 500, 10_000)   # Ineligible: credit score too low
run_loan_check(90_000, 780, 20_000)   # Approved: Premium
run_loan_check(55_000, 670, 15_000)   # Approved: Standard
run_loan_check(35_000, 610, 8_000)    # Approved: Higher risk
run_loan_check("abc", 700, 10_000)    # ValueError caught
```

### Expected Output
```
Ineligible: income below minimum threshold

Ineligible: credit score too low

Approved: Premium rate (4.5%)
  → Estimated monthly payment: $75.00

Approved: Standard rate (6.5%)
  → Estimated monthly payment: $81.25

Approved: Higher risk rate (9.9%)
  → Estimated monthly payment: $66.00

Error: income, credit score, and loan amount must all be numbers.
```

### Key Concepts

| Concept | Explanation |
|---|---|
| Ineligibility before approval | Hard disqualifiers (`income < 30k`, `credit_score < 580`) are checked first to short-circuit — no need to evaluate approval tiers for someone who already fails |
| Compound conditions (`and`) | Both income AND credit score must meet the threshold to qualify for a tier |
| `try/except ValueError` | Wraps the conversion `float(income)` — if someone passes `"abc"`, Python raises a `ValueError` which we catch cleanly |
| `result.startswith("Approved")` | A clean way to check whether to print a monthly payment without needing a separate boolean flag |
| Underscore in numbers | `80_000` is identical to `80000` in Python — the underscore is just a visual separator for readability |

> **Order matters in multi-condition logic.** The Premium tier must be checked before Standard — a person with `income=90,000` and `credit_score=780` satisfies *both* Premium and Standard conditions. Checking Premium first ensures they get the correct (better) rate.

---

## Exercise 3 — Sales Report Generator (20 pts)

### Solution

```python
def compute_stats(sales):
    """Compute summary statistics for a list of sales figures.

    Args:
        sales (list of int/float): Sales totals per representative.

    Returns:
        dict: Keys 'total', 'average', 'highest', 'lowest', 'top_index'.
    """
    total = sum(sales)
    average = total / len(sales)
    highest = max(sales)
    lowest = min(sales)
    top_index = sales.index(highest)   # Position of the top performer

    return {
        "total":     total,
        "average":   average,
        "highest":   highest,
        "lowest":    lowest,
        "top_index": top_index,
    }


def print_report(reps, sales):
    """Print a formatted sales report with a text bar chart.

    Uses enumerate() to loop over reps and sales together.
    Marks the top performer and prints a █ bar for every $1,000 in sales.

    Args:
        reps (list of str): Sales representative names.
        sales (list of int/float): Corresponding sales figures.
    """
    stats = compute_stats(sales)

    print("=" * 40)
    print("         SALES REPORT")
    print("=" * 40)

    for i, (rep, amount) in enumerate(zip(reps, sales)):
        # Flag the top performer
        tag = "  ◀ Top performer" if i == stats["top_index"] else ""

        # Build the bar: one █ per $1,000 (int division)
        bar = "█" * (amount // 1_000)

        print(f"{rep:<8} ${amount:>6,}  {bar}{tag}")

    print("-" * 40)
    print(f"Total:    ${stats['total']:>8,}")
    print(f"Average:  ${stats['average']:>8,.0f}")
    print(f"Highest:  ${stats['highest']:>8,}")
    print(f"Lowest:   ${stats['lowest']:>8,}")
    print("=" * 40)


# --- Hard-coded dataset ---
reps  = ['Alice', 'Bob', 'Carol', 'David', 'Eva']
sales = [12400, 8300, 15600, 6700, 9800]

print_report(reps, sales)
```

### Expected Output
```
========================================
         SALES REPORT
========================================
Alice    $ 12,400  ████████████
Bob      $  8,300  ████████
Carol    $ 15,600  ███████████████  ◀ Top performer
David    $  6,700  ██████
Eva      $  9,800  █████████
----------------------------------------
Total:    $  52,800
Average:  $  10,560
Highest:  $  15,600
Lowest:   $   6,700
========================================
```

### Key Concepts

| Concept | Explanation |
|---|---|
| `enumerate()` | Gives you both the index `i` and the value in one loop — no need to manually track a counter |
| `zip(reps, sales)` | Pairs each rep with their sales figure so you can loop over both lists simultaneously |
| `list.index()` | Returns the position of the first occurrence of a value — used here to find which rep had the highest sales |
| `//` (floor division) | `15600 // 1000` gives `15` — the whole number of thousands, which is how many `█` to print |
| `"█" * n` | String multiplication — repeats the character `n` times to build the bar |
| f-string alignment `:<8` and `:>6,` | `<` left-aligns, `>` right-aligns, the number is the field width, `,` adds thousands separators |
| Returning a `dict` from a function | Packing multiple return values into a dictionary keeps the function's return value readable and extensible |

> **Why two functions?** `compute_stats()` handles the math and `print_report()` handles the display. This separation means you could reuse `compute_stats()` elsewhere (e.g. to feed a chart or a database) without it being tied to printing. This is the **single responsibility principle** — each function does one job.

---

## Quick Reference — Control Structures & Functions

| Concept | Syntax | Notes |
|---|---|---|
| `if / elif / else` | `if x > 10: ...` | Check from most to least specific |
| `and` / `or` | `if a >= 50 and b >= 650` | Both (`and`) / either (`or`) must be true |
| `for` with `enumerate` | `for i, val in enumerate(lst)` | Gets index and value together |
| `for` with `zip` | `for a, b in zip(list1, list2)` | Loops two lists in parallel |
| `try / except` | `try: ... except ValueError: ...` | Catches specific error types cleanly |
| Function definition | `def my_func(arg):` | Always add a docstring on the next line |
| Docstring | `"""Does X. Args: ... Returns: ..."""` | Required for every function in this course |
| Floor division | `x // 1000` | Drops the remainder — useful for bar charts, bucketing |
| String repeat | `"█" * n` | Builds repeated patterns without a loop |
