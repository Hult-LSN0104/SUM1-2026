# =============================================================================
# LSN-0104 | Week 6, Session 11
# File Handling — Reading and Writing Data / CSV Files
# =============================================================================
#
# So far your programs have lost all their data when they finished.
# Files let you save data permanently and read it back later.
#
# Opening and reading a text file:
#   with open("filename.txt", "r") as f:
#       contents = f.read()         # entire file as one string
#       # OR
#       lines = f.readlines()       # list of lines
#       # OR
#       for line in f:              # one line at a time
#           print(line.strip())
#
# Writing to a text file:
#   with open("output.txt", "w") as f:   # "w" overwrites, "a" appends
#       f.write("Hello\n")
#
# File modes:
#   "r"  — read (file must exist)
#   "w"  — write (creates or overwrites)
#   "a"  — append (adds to end of existing file)
#
# Reading CSV files with the csv module:
#   import csv
#   with open("data.csv", "r") as f:
#       reader = csv.DictReader(f)       # each row becomes a dictionary
#       for row in reader:
#           print(row["column_name"])
#
# Writing CSV files:
#   with open("output.csv", "w", newline="") as f:
#       writer = csv.DictWriter(f, fieldnames=["col1", "col2"])
#       writer.writeheader()
#       writer.writerow({"col1": "value1", "col2": "value2"})
#
# YOUR TASK
# ---------
# Read a sales CSV file, analyse the data, and write a summary report.
# The file `sales.csv` is in the `datasets/` folder of this repo.
#
# sales.csv columns:
#   date, rep_name, region, product, quantity, unit_price
#
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================

import csv
import os


# Path to the data file — adjust if you're running from a different location
DATA_FILE   = "../../datasets/sales.csv"
REPORT_FILE = "sales_report.txt"


# -----------------------------------------------------------------------------
# PART 1 — Read the CSV and load the data into a list of dictionaries
# -----------------------------------------------------------------------------
#
# Open DATA_FILE with csv.DictReader.
# Append each row to a list called `sales`.
# After loading, print how many records were found.
#
# 👉 YOUR CODE HERE

sales = []

with open(DATA_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        


print(f"Loaded {len(sales)} sales records.")


# -----------------------------------------------------------------------------
# PART 2 — Calculate the total revenue per region
# -----------------------------------------------------------------------------
#
# revenue = quantity * unit_price   (both stored as strings — convert them!)
#
# Build a dictionary called region_totals:
#   { "North": 45230.50, "South": 38100.00, ... }
#
# Print each region and its total revenue.
#
# 👉 YOUR CODE HERE

region_totals = {}

for row in sales:
    region  = row["region"]
    revenue = 
    
    if region not in region_totals:
        region_totals[region] = 0
    region_totals[region] += revenue

print("\n--- Revenue by Region ---")
for region, total in sorted(region_totals.items()):
    print(f"  {region:<12} ${total:>12,.2f}")


# -----------------------------------------------------------------------------
# PART 3 — Find the top-selling product by quantity
# -----------------------------------------------------------------------------
#
# Build a dictionary called product_quantities:
#   { "Laptop Stand": 230, "Wireless Mouse": 415, ... }
#
# Then find the product with the highest total quantity sold.
#
# 👉 YOUR CODE HERE

product_quantities = {}

for row in sales:
    product  = row["product"]
    quantity = 
    
    if product not in product_quantities:
        product_quantities[product] = 0
    product_quantities[product] += quantity

top_product = max(product_quantities, key=product_quantities.get)
print(f"\n🏆 Top product: {top_product} ({product_quantities[top_product]:,} units)")


# -----------------------------------------------------------------------------
# PART 4 — Write a formatted summary report to a text file
# -----------------------------------------------------------------------------
#
# Write a report to REPORT_FILE that includes:
#   - Total records processed
#   - Revenue by region (from Part 2)
#   - Top product (from Part 3)
#   - Overall total revenue across all regions
#
# Use "w" mode. Use f.write() — remember to add \n for new lines.
#
# 👉 YOUR CODE HERE

overall_total = sum(region_totals.values())

with open(REPORT_FILE, "w") as f:
    f.write("SALES SUMMARY REPORT\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total records processed: {len(sales)}\n\n")
    
    f.write("Revenue by Region:\n")
    for region, total in sorted(region_totals.items()):
        f.write(f"  {region:<12} ${total:>12,.2f}\n")
    
    f.write(f"\nTop Product: {top_product} ({product_quantities[top_product]:,} units)\n")
    f.write(f"\nOverall Total Revenue: ${overall_total:,.2f}\n")

print(f"\n✓ Report saved to {REPORT_FILE}")


# -----------------------------------------------------------------------------
# PART 5 — Write a filtered CSV of just the top region's sales
# -----------------------------------------------------------------------------
#
# Find the region with the highest revenue.
# Write a new CSV file called `top_region_sales.csv` containing only
# the rows from that region. Include the header row.
#
# 👉 YOUR CODE HERE

top_region = max(region_totals, key=region_totals.get)
output_csv = "top_region_sales.csv"

with open(output_csv, "w", newline="") as f:
    fieldnames = ["date", "rep_name", "region", "product", "quantity", "unit_price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in sales:
        if row["region"] == top_region:
            

print(f"✓ Saved {top_region} sales to {output_csv}")


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Calculate revenue per sales rep and add a "Top Rep" line to the report.
#
#   2. Add a function called load_sales(filepath) that wraps the file reading
#      logic from Part 1 — so you can reuse it in the capstone.
#
#   3. Add error handling: if DATA_FILE doesn't exist, print a clear message
#      instead of crashing. Use try/except FileNotFoundError.
# =============================================================================