# =============================================================================
# LSN-0104 | Problem Set 2 — Sales Data Cleaner & Formatter
# =============================================================================
#
# Instructions are in instructions.md
# =============================================================================

# The raw data — do not change these values
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


# -----------------------------------------------------------------------------
# STEP 1 — Parse and clean each record
# -----------------------------------------------------------------------------
# Loop through raw_records.
# For each one, split on "|", clean each field, and store the results.
# Build a list called `clean_records` — a list of lists or list of tuples.

# 👉 YOUR CODE HERE

clean_records = []

for record in raw_records:
    parts = record.split("|")
    
    rep      = 
    product  = 
    quantity = 
    price    = 
    
    clean_records.append([rep, product, quantity, price])


# -----------------------------------------------------------------------------
# STEP 2 — Calculate line totals and print the table
# -----------------------------------------------------------------------------
# Print a header row, then one line per record.
# Include the line total (quantity * price) in the last column.

# 👉 YOUR CODE HERE

print(f"{'Rep':<18}{'Product':<30}{'Qty':>5}{'Unit Price':>12}{'Line Total':>12}")
print("-" * 78)

for record in clean_records:
    rep, product, quantity, price = record
    line_total = 
    print(f"")


# -----------------------------------------------------------------------------
# STEP 3 — Print the summary section
# -----------------------------------------------------------------------------
# Total records, grand total revenue, rep with highest combined sales.

# 👉 YOUR CODE HERE
