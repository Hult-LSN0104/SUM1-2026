# =============================================================================
# LSN-0104 | Week 6, Session 12
# Capstone — Customer Sales Report Generator
# =============================================================================
#
# This is it. Everything you've built over six weeks comes together here.
#
# You'll write a complete, end-to-end program that:
#   1. Loads customer transaction data from a CSV file
#   2. Processes it using functions, loops, and dictionaries
#   3. Applies business logic (discounts, tier classification)
#   4. Writes a formatted report to a text file
#   5. Saves a summary CSV ready to share with colleagues
#
# The file `transactions.csv` is in the `capstone/` folder of this repo.
#
# transactions.csv columns:
#   transaction_id, customer_id, customer_name, product,
#   quantity, unit_price, date
#
# There are no "right answers" for stretch goals or presentation style —
# this is your program. Make it yours.
#
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================

import csv
import os
from datetime import datetime


# Configuration — adjust paths if needed
DATA_FILE    = "../../capstone/transactions.csv"
REPORT_FILE  = "customer_report.txt"
SUMMARY_CSV  = "customer_summary.csv"

# Discount tiers based on total spend
DISCOUNT_TIERS = [
    (5000, 0.15),   # spend >= $5,000 → 15% discount
    (2000, 0.10),   # spend >= $2,000 → 10% discount
    (500,  0.05),   # spend >= $500   →  5% discount
    (0,    0.00),   # below $500      →  no discount
]

# Customer tier labels based on total spend
TIER_LABELS = [
    (5000, "Platinum"),
    (2000, "Gold"),
    (500,  "Standard"),
    (0,    "New"),
]


# =============================================================================
# PART 1 — Data loading
# =============================================================================

def load_transactions(filepath):
    """Load transactions from a CSV file and return a list of dictionaries."""
    transactions = []
    # 👉 YOUR CODE HERE: open the file, use csv.DictReader, append each row
    #    Convert quantity to int and unit_price to float before appending.
    
    
    return transactions


# =============================================================================
# PART 2 — Business logic helpers
# =============================================================================

def calculate_line_total(quantity, unit_price):
    """Return the total value for a single transaction line."""
    # 👉 YOUR CODE HERE
    


def get_discount_rate(total_spend):
    """Return the discount rate for a given total spend amount."""
    # 👉 YOUR CODE HERE: loop through DISCOUNT_TIERS and return the right rate
    for threshold, rate in DISCOUNT_TIERS:
        if total_spend >= threshold:
            return rate


def get_customer_tier(total_spend):
    """Return the tier label for a given total spend amount."""
    # 👉 YOUR CODE HERE: same pattern as get_discount_rate
    for threshold, label in TIER_LABELS:
        if total_spend >= threshold:
            return label


def apply_discount(amount, rate):
    """Return the amount after applying a discount rate."""
    # 👉 YOUR CODE HERE
    


# =============================================================================
# PART 3 — Build customer summaries
# =============================================================================

def build_customer_summaries(transactions):
    """
    Process all transactions and return a dictionary of customer summaries.
    
    Each key is a customer_id. Each value is a dictionary with:
        name, total_spend, discounted_spend, discount_rate,
        tier, transaction_count, products (list of unique products)
    """
    summaries = {}
    
    # 👉 YOUR CODE HERE
    # Loop through transactions. For each one:
    #   - Calculate the line total using calculate_line_total()
    #   - If the customer isn't in summaries yet, add them with starting values
    #   - Add the line total to their running total_spend
    #   - Track their unique products (hint: use a list and check `if not in`)
    #   - Increment their transaction_count
    #
    # After building the totals, loop through summaries again to:
    #   - Set discount_rate using get_discount_rate()
    #   - Set discounted_spend using apply_discount()
    #   - Set tier using get_customer_tier()
    
    
    return summaries


# =============================================================================
# PART 4 — Write the text report
# =============================================================================

def write_report(summaries, output_path):
    """Write a formatted customer report to a text file."""
    
    # Sort by discounted_spend, highest first
    sorted_customers = sorted(
        summaries.items(),
        key=lambda x: x[1]["discounted_spend"],
        reverse=True
    )
    
    # 👉 YOUR CODE HERE
    # Open output_path in write mode and write:
    #   - A title and generation timestamp  (use datetime.now())
    #   - A divider line
    #   - One section per customer showing:
    #       Customer ID, name, tier
    #       Transaction count, unique products
    #       Total spend (before discount)
    #       Discount rate and discount amount
    #       Final spend (after discount)
    #   - A grand totals section at the bottom:
    #       Total customers, total transactions,
    #       Total revenue (pre-discount), total revenue (post-discount)
    
    with open(output_path, "w") as f:
        f.write("CUSTOMER SALES REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("=" * 50 + "\n\n")
        
        for customer_id, c in sorted_customers:
            


# =============================================================================
# PART 5 — Write the summary CSV
# =============================================================================

def write_summary_csv(summaries, output_path):
    """Write a one-row-per-customer summary CSV file."""
    fieldnames = [
        "customer_id", "customer_name", "tier",
        "transaction_count", "total_spend",
        "discount_rate", "discounted_spend"
    ]
    
    # 👉 YOUR CODE HERE: open output_path with csv.DictWriter
    #    Write the header, then one row per customer
    
    


# =============================================================================
# PART 6 — Main program
# =============================================================================

def main():
    """Run the full report generation pipeline."""
    
    print("Customer Sales Report Generator")
    print("=" * 35)
    
    # Step 1 — Load
    print(f"\nLoading data from {DATA_FILE}...")
    # 👉 YOUR CODE HERE: call load_transactions() and print how many loaded
    
    
    # Step 2 — Process
    print("Processing transactions...")
    # 👉 YOUR CODE HERE: call build_customer_summaries()
    
    
    # Step 3 — Report
    print(f"Writing report to {REPORT_FILE}...")
    # 👉 YOUR CODE HERE: call write_report()
    
    
    # Step 4 — CSV
    print(f"Writing summary CSV to {SUMMARY_CSV}...")
    # 👉 YOUR CODE HERE: call write_summary_csv()
    
    
    print("\n✓ Done! Files saved:")
    print(f"   {REPORT_FILE}")
    print(f"   {SUMMARY_CSV}")
    
    # Step 5 — Preview
    # 👉 YOUR CODE HERE (optional): print the top 3 customers by discounted spend
    print("\n--- Top Customers ---")


# Run the program
if __name__ == "__main__":
    main()


# =============================================================================
# STRETCH CHALLENGES / PRESENTATION IDEAS
#
#   1. Add a "monthly breakdown" section to the report — group transactions
#      by month and show revenue per month across all customers.
#
#   2. Add a function that identifies customers whose spend has dropped
#      compared to last month — potential churn risk.
#
#   3. Deployment: share your Colab notebook link with a classmate.
#      Can they run your program on the same dataset and get the same output?
#      That's the real test of whether your code works for someone else.
#
#   4. What would you need to change to make this work with a different
#      company's data? What are the "hardcoded" assumptions in your program?
# =============================================================================