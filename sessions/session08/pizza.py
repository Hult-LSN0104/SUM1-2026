import csv
import sys
from tabulate import tabulate


def load_menu(filename):
    """Load a CSV menu file and return headers + rows."""
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    headers = rows[0]
    data = rows[1:]
    return headers, data


def main():
    # Step 1: Ask for menu type
    while True:
        choice = input("Which menu would you like? (Sicilian / Regular): ").strip().lower()
        if choice == "sicilian":
            filename = "sicilian.csv"
            break
        elif choice == "regular":
            filename = "regular.csv"
            break
        else:
            print("Invalid choice. Please enter Sicilian or Regular.")

    # Step 2: Load and display the menu
    try:
        headers, data = load_menu(filename)
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'.")
        sys.exit(1)

    print()
    print(tabulate(data, headers=headers, tablefmt="grid"))
    print()

    # Step 3: Ask which pizza they want
    pizza_names = [row[0].lower() for row in data]
    while True:
        selection = input("Which pizza would you like? ").strip().lower()
        matched = next((row for row in data if row[0].lower() == selection), None)
        if matched:
            print(f"\nYou selected: {matched[0]}")
            print(f"  Small: {matched[1]}")
            print(f"  Large: {matched[2]}")
            break
        else:
            print(f"Invalid selection. Choose from: {', '.join(row[0] for row in data)}")

    print("\nThank you! Goodbye.")
    sys.exit(0)


if __name__ == "__main__":
    main()

# The trickiest part was handling the CSV header row cleanly. The csv.reader returns all rows
# including the header, so I had to slice rows[0] as headers and rows[1:] as data before passing
# to tabulate. A secondary challenge was making the menu matching case-insensitive while still
# producing a meaningful error message for truly invalid input, without accidentally swallowing
# a legitimate FileNotFoundError from a missing CSV file.