# =============================================================================
# LSN-0104 | Problem Set 4 — Payroll Calculator
# =============================================================================
#
# Instructions are in instructions.md
# Write each function, then run the employee list through them.
# =============================================================================

# Constants — reference these inside your functions, don't hardcode the numbers
OVERTIME_THRESHOLD   = 40
OVERTIME_MULTIPLIER  = 1.5
FEDERAL_TAX_RATE     = 0.22
STATE_TAX_RATE       = 0.05
HEALTH_INSURANCE_FEE = 85.00

# Employee data — do not change
employees = [
    {"name": "Alice Johnson",  "role": "Sales Manager",    "type": "full_time",  "hours": 42.0, "rate": 28.50},
    {"name": "Bob Smith",      "role": "Sales Rep",        "type": "full_time",  "hours": 40.0, "rate": 22.00},
    {"name": "Carol White",    "role": "Lead Developer",   "type": "full_time",  "hours": 45.5, "rate": 45.00},
    {"name": "David Lee",      "role": "Marketing Coord.", "type": "part_time",  "hours": 20.0, "rate": 18.00},
    {"name": "Elena Garcia",   "role": "Data Analyst",     "type": "full_time",  "hours": 38.0, "rate": 35.00},
    {"name": "Frank Nguyen",   "role": "Support Agent",    "type": "part_time",  "hours": 25.5, "rate": 16.50},
]


# -----------------------------------------------------------------------------
# FUNCTION 1 — calculate_gross_pay
# -----------------------------------------------------------------------------

def calculate_gross_pay(hours, rate):
    """
    Calculate gross pay including overtime.
    Raises ValueError if hours or rate are invalid.
    """
    # 👉 YOUR CODE HERE
    # Validate inputs first
    
    # Calculate regular and overtime pay
    if hours > OVERTIME_THRESHOLD:
        regular_pay  = 
        overtime_pay = 
    else:
        regular_pay  = 
        overtime_pay = 0
    
    return regular_pay + overtime_pay


# -----------------------------------------------------------------------------
# FUNCTION 2 — calculate_deductions
# -----------------------------------------------------------------------------

def calculate_deductions(gross_pay, employee_type):
    """
    Calculate and return all deductions as a dictionary.
    Keys: federal_tax, state_tax, health_insurance, total
    """
    # 👉 YOUR CODE HERE
    federal_tax      = 
    state_tax        = 
    health_insurance = HEALTH_INSURANCE_FEE if employee_type == "full_time" else 0
    total            = 
    
    return {
        "federal_tax":      federal_tax,
        "state_tax":        state_tax,
        "health_insurance": health_insurance,
        "total":            total,
    }


# -----------------------------------------------------------------------------
# FUNCTION 3 — calculate_net_pay
# -----------------------------------------------------------------------------

def calculate_net_pay(gross_pay, deductions):
    """Return net pay after all deductions."""
    # 👉 YOUR CODE HERE


# -----------------------------------------------------------------------------
# FUNCTION 4 — print_pay_stub
# -----------------------------------------------------------------------------

def print_pay_stub(employee, gross, deductions, net):
    """Print a formatted pay stub for one employee."""
    # 👉 YOUR CODE HERE
    print("=" * 42)
    print(f"  PAY STUB — {employee['name']}")
    print(f"  Role: {employee['role']} | {employee['type'].replace('_', ' ').title()}")
    print("=" * 42)
    # ... continue formatting
    print()


# -----------------------------------------------------------------------------
# MAIN — Process all employees
# -----------------------------------------------------------------------------

total_gross      = 0.0
total_deductions = 0.0
total_net        = 0.0
top_employee     = None
top_net          = 0.0

for emp in employees:
    try:
        gross      = calculate_gross_pay(emp["hours"], emp["rate"])
        deductions = calculate_deductions(gross, emp["type"])
        net        = calculate_net_pay(gross, deductions)
        
        print_pay_stub(emp, gross, deductions, net)
        
        total_gross      += gross
        total_deductions += deductions["total"]
        total_net        += net
        
        if net > top_net:
            top_net      = net
            top_employee = emp["name"]
    
    except ValueError as e:
        print(f"Error processing {emp['name']}: {e}")


# -----------------------------------------------------------------------------
# PAYROLL SUMMARY
# -----------------------------------------------------------------------------

# 👉 YOUR CODE HERE
print("=" * 42)
print("  PAYROLL SUMMARY")
print("=" * 42)
