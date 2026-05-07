# Problem Set 1 — Business Card Generator
**LSN-0104 | Due: Before Session 3**
**Weight: 6% of final grade**

---

## Overview

You've learned how to store information in variables, work with Python's core data types, and print formatted output. Now put it together in a small, complete program.

You'll build a **Business Card Generator** — a program that asks a user for their professional details and prints a formatted business card to the screen.

---

## Requirements

Your program must:

1. **Collect the following information from the user** using `input()`:
   - Full name
   - Job title
   - Company name
   - Email address
   - Phone number
   - City and country

2. **Store each value in a clearly named variable** with an appropriate data type.

3. **Print a formatted business card** that looks something like this:

```
╔══════════════════════════════════════╗
  Alice Johnson
  Head of Product
  Northbridge Solutions

  alice.johnson@northbridge.com
  +1 617-555-0101
  Boston, United States
╚══════════════════════════════════════╝
```

You don't have to use the exact box style above — but the card should be clearly laid out and easy to read.

4. **Use at least one f-string** to build the output.

5. **Include at least three comments** explaining what your code does.

---

## Hints

- `input()` always returns a string — that's fine for all fields in this program.
- To print a line of repeated characters: `print("=" * 40)`
- You can use `\n` inside a string to add a blank line: `print("line one\nline two")`
- Keep your variable names descriptive: `full_name` is better than `n`.

---

## Stretch Goals *(optional, no extra marks)*

- Ask the user for their LinkedIn URL and include it on the card.
- Print the name in ALL CAPS using a string method.
- Print two cards side by side for two different people.

---

## Submission

Upload your completed `starter.py` file to Canvas by the deadline.
Your file should run without errors from top to bottom.

---

## Grading

| Criterion | Marks |
|-----------|-------|
| Program runs without errors | 3 |
| All six fields collected and stored in variables | 2 |
| Output is clearly formatted and readable | 3 |
| At least one f-string used | 1 |
| At least three comments present | 1 |
| **Total** | **10** |
