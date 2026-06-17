"""
LSN-0104 — Introduction to Programming with Python
Problem Set 2: Control Structures & Functions

Author: <Abigail Adugna>
"""


# =============================================================================
# Exercise 1 — Tiered Discount Engine (20 pts)
# =============================================================================

def get_discount(order_total):
    """
    Return the discount rate (as a decimal) for a given order total.

    Tiers:
        $0      – $99.99    -> 0.00
        $100    – $499.99   -> 0.05
        $500    – $999.99   -> 0.10
        $1,000+             -> 0.20
    """
    if order_total >= 1000:
        return 0.20
    elif order_total >= 500:
        return 0.10
    elif order_total >= 100:
        return 0.05
    else:
        return 0.00


def apply_discount(order_total):
    """
    Apply the tier discount to `order_total`.

    Calls get_discount() to retrieve the rate, prints a message of the form:
        "$750.00 order qualifies for a 10% discount. Final price: $675.00"
    Returns the final price after discount.
    """
    rate = get_discount(order_total)
    final_price = order_total - (order_total * rate)

    print(f"${order_total:.2f} order qualifies for a {rate:.0%} discount. Final price: ${final_price:.2f}")

    return final_price


# =============================================================================
# Exercise 2 — Loan Eligibility System (20 pts)
# =============================================================================

def check_loan(income, credit_score, loan_amount):
    """
    Determine loan eligibility and print the decision.

    Logic:
        income < 30,000                               -> 'Ineligible: income below minimum threshold'
        credit_score < 580                            -> 'Ineligible: credit score too low'
        income >= 80,000 and credit_score >= 750      -> 'Approved: Premium rate (4.5%)'
        income >= 50,000 and credit_score >= 650      -> 'Approved: Standard rate (6.5%)'
        otherwise                                     -> 'Approved: Higher risk rate (9.9%)'

    For approved loans, also print the estimated monthly payment:
        monthly = (loan_amount * rate) / 12
    where `rate` is the annual interest rate as a decimal (e.g. 0.045).
    """

    income = float(income)
    credit_score = int(credit_score)
    loan_amount = float(loan_amount)

    if income < 30000:
        print("Ineligible: income below minimum threshold")
        return "Ineligible: income below minimum threshold"

    if credit_score < 580:
        print("Ineligible: credit score too low")
        return "Ineligible: credit score too low"

    if income >= 80000 and credit_score >= 750:
        rate = 0.045
        decision = "Approved: Premium rate (4.5%)"
    elif income >= 50000 and credit_score >= 650:
        rate = 0.065
        decision = "Approved: Standard rate (6.5%)"
    else:
        rate = 0.099
        decision = "Approved: Higher risk rate (9.9%)"

    monthly = (loan_amount * rate) / 12

    print(decision)
    print(f"Estimated monthly payment: ${monthly:.2f}")

    return decision




# =============================================================================
# Exercise 3 — Sales Report Generator (20 pts)
# =============================================================================

reps  = ["Alice", "Bob", "Carol", "David", "Eva"]
sales = [12400, 8300, 15600, 6700, 9800]


def compute_stats(sales):
    """
    Return total, average, highest, and lowest sales.
    Suggested return type: a dict like
        {"total": ..., "average": ..., "highest": ..., "lowest": ...}
    """
    total = sum(sales)
    average = total / len(sales)
    highest = max(sales)
    lowest = min(sales)

    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }


def print_report(reps, sales):
    """
    Print the full sales report:
      - For each rep: name and sales (use enumerate())
      - 'Top performer' tag next to the rep with the highest sales
      - Total, average, highest, lowest (call compute_stats())
      - A simple bar chart: each $1,000 in sales = one '█' character
    """
    stats = compute_stats(sales)

    print("Sales Report")
    print("------------")

    for index, rep in enumerate(reps):
        sales_amount = sales[index]

        if sales_amount == stats["highest"]:
            print(f"{rep}: ${sales_amount} Top performer")
        else:
            print(f"{rep}: ${sales_amount}")

    print("\nStatistics")
    print("----------")
    print(f"Total sales: ${stats['total']}")
    print(f"Average sales: ${stats['average']:.2f}")
    print(f"Highest sales: ${stats['highest']}")
    print(f"Lowest sales: ${stats['lowest']}")

    print("\nBar Chart")
    print("---------")

    for index, rep in enumerate(reps):
        bar = "█" * (sales[index] // 1000)
        print(f"{rep}: {bar}")

# =============================================================================
# Main — test cases
# =============================================================================

if __name__ == "__main__":
    # ---- Exercise 1: test all four tiers ----
    # apply_discount(50)        # 0%
    # apply_discount(250)       # 5%
    # apply_discount(750)       # 10%
    # apply_discount(1500)      # 20%

    # ---- Exercise 2: wrap calls in try/except for ValueError; test 5 scenarios ----
    # try:
    #     check_loan(25_000, 700, 10_000)   # ineligible — income
    #     check_loan(60_000, 550, 20_000)   # ineligible — credit
    #     check_loan(90_000, 780, 250_000)  # premium
    #     check_loan(60_000, 680, 150_000)  # standard
    #     check_loan(40_000, 620,  50_000)  # higher risk
    # except ValueError as e:
    #     print(f"Invalid input: {e}")

    # ---- Exercise 3 ----
    # print_report(reps, sales)

        pass 

    
