# =============================================================================
# LSN-0104 | Week 3, Session 6
# Control Structures: Loops
# =============================================================================
#
# Loops let you repeat code without writing it out over and over.
#
# FOR loop — use when you know what you're iterating over:
#   for item in collection:
#       # do something with item
#
#   for i in range(5):      # i goes 0, 1, 2, 3, 4
#       print(i)
#
# WHILE loop — use when you repeat until a condition is met:
#   while condition:
#       # do something
#
# Loop control:
#   break     — exit the loop immediately
#   continue  — skip the rest of this iteration, move to the next
#   pass      — do nothing (placeholder)
#
# Useful with loops:
#   sum()     total of a list:       sum([10, 20, 30])  →  60
#   len()     number of items:       len([10, 20, 30])  →  3
#   min()     smallest value:        min([10, 20, 30])  →  10
#   max()     largest value:         max([10, 20, 30])  →  30
#
# YOUR TASK
# ---------
# Process a list of weekly sales figures and generate a summary report.
# Look for lines marked with:  👉 YOUR CODE HERE
#
# =============================================================================


# Sales data — weekly revenue figures ($) for five sales reps
# Do not change these values.
sales_reps = ["Alice", "Bob", "Carol", "David", "Elena"]
weekly_sales = [
    [12400, 9800, 11200, 13500, 10900, 12100, 11800],   # Alice
    [8500,  9200, 7800,  10200, 9600,  8900,  9100],    # Bob
    [15200, 14800, 16100, 13900, 15600, 14200, 16800],  # Carol
    [6200,  7100,  5800,  6900,  7400,  6600,  7200],   # David
    [11100, 10800, 12200, 11500, 10600, 11900, 12400],  # Elena
]


# -----------------------------------------------------------------------------
# PART 1 — Print each rep's weekly figures
# -----------------------------------------------------------------------------
#
# Loop through both lists at the same time using zip().
# zip() pairs up two lists: zip(sales_reps, weekly_sales)
#
# Print each rep's name followed by their list of weekly figures.
# Example output:
#   Alice:  [12400, 9800, 11200, 13500, 10900, 12100, 11800]
#
# 👉 YOUR CODE HERE

print("--- Weekly Sales Figures ---")
for rep, figures in zip(sales_reps, weekly_sales):



# -----------------------------------------------------------------------------
# PART 2 — Calculate totals and averages for each rep
# -----------------------------------------------------------------------------
#
# For each rep, calculate:
#   total    = sum of their weekly figures
#   average  = total divided by number of weeks
#
# Print one summary line per rep. Example:
#   Alice  |  Total: $79,700  |  Weekly Avg: $11,385.71
#
# 👉 YOUR CODE HERE

print("\n--- Per-Rep Summary ---")
for rep, figures in zip(sales_reps, weekly_sales):
    total = 
    average = 
    print(f"")


# -----------------------------------------------------------------------------
# PART 3 — Find the top performer
# -----------------------------------------------------------------------------
#
# Loop through the totals you calculated above and find:
#   best_rep    — the name of the rep with the highest total
#   best_total  — their total sales figure
#
# 👉 YOUR CODE HERE

best_rep = ""
best_total = 0

for rep, figures in zip(sales_reps, weekly_sales):
    total = sum(figures)
    if :
        best_rep = 
        best_total = 

print(f"\n🏆 Top performer: {best_rep} with ${best_total:,}")


# -----------------------------------------------------------------------------
# PART 4 — Flag any rep whose weekly sales dropped below $8,000
# -----------------------------------------------------------------------------
#
# Loop through each rep's figures. If any individual week is below 8000,
# print a warning. Example:
#   ⚠️  David had a low week: $5,800 (week 3)
#
# Hint: use enumerate() to get both the index and value:
#   for week_num, amount in enumerate(figures, start=1):
#
# 👉 YOUR CODE HERE

THRESHOLD = 8000
print("\n--- Low Week Alerts ---")

for rep, figures in zip(sales_reps, weekly_sales):
    for week_num, amount in enumerate(figures, start=1):
        if :
            print(f"")


# =============================================================================
# STRETCH CHALLENGES
#
#   1. Calculate the overall team total and team weekly average across
#      all reps combined.
#
#   2. Add a while loop that keeps asking the user to type a rep's name
#      until they type "quit". For each name entered, print that rep's total.
#
#   3. Sort the reps from highest to lowest total and print a ranked
#      leaderboard. Hint: look up the sorted() function.
# =============================================================================