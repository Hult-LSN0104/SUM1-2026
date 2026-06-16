import sys
from tabulate import tabulate

# Hardcoded data from FakeStore API
PRODUCTS = [
    [1, "Fjallraven Backpack", "$109.95", "men's clothing"],
    [2, "Mens Casual Premium Slim Fit T-Shirts", "$22.30", "men's clothing"],
    [3, "Mens Cotton Jacket", "$55.99", "men's clothing"],
    [4, "Mens Casual Slim Fit Pants", "$15.99", "men's clothing"],
    [5, "John Hardy Bracelet", "$695.00", "jewelery"],
    [6, "Solid Gold Petite Micropave Ring", "$168.00", "jewelery"],
    [7, "White Gold Plated Princess Ring", "$9.99", "jewelery"],
    [8, "Pierced Owl Rose Gold Plated Earrings", "$10.99", "jewelery"],
    [9, "WD 2TB Elements Portable Hard Drive", "$64.00", "electronics"],
    [10, "SanDisk 1TB Ultra microSDXC", "$109.00", "electronics"],
    [11, "Silicon Power 256GB Card", "$109.00", "electronics"],
    [12, "WD 4TB Gaming Drive", "$114.00", "electronics"],
    [13, "Acer SB220Q 21.5 inch Monitor", "$599.00", "electronics"],
    [14, "Samsung 49-Inch CHG90 Monitor", "$999.99", "electronics"],
    [15, "BIYLACLESEN Women's 3-in-1 Jacket", "$56.99", "women's clothing"],
    [16, "Lock and Love Quilted Leather Jacket", "$29.95", "women's clothing"],
    [17, "Rain Jacket Women Windbreaker", "$39.99", "women's clothing"],
    [18, "MBJ Women's Solid Short Sleeve Boat Neck V", "$9.85", "women's clothing"],
    [19, "Opna Women's Short Sleeve Moisture", "$7.95", "women's clothing"],
    [20, "DANVOUY Womens T Shirt Casual Cotton", "$12.99", "women's clothing"],
]

CATEGORIES = [
    [1, "electronics"],
    [2, "jewelery"],
    [3, "men's clothing"],
    [4, "women's clothing"],
]

CARTS = [
    [1, 1, 3, 6],
    [2, 1, 2, 4],
    [3, 2, 4, 9],
    [4, 3, 2, 3],
    [5, 3, 1, 2],
    [6, 4, 3, 7],
    [7, 8, 2, 5],
]


def show_products():
    headers = ["ID", "Title", "Price", "Category"]
    print()
    print(tabulate(PRODUCTS, headers=headers, tablefmt="grid"))
    print()


def show_categories():
    headers = ["#", "Category"]
    print()
    print(tabulate(CATEGORIES, headers=headers, tablefmt="grid"))
    print()


def show_carts():
    headers = ["Cart ID", "User ID", "Unique Items", "Total Items"]
    print()
    print(tabulate(CARTS, headers=headers, tablefmt="grid"))
    print()


MENU = {
    "1": ("Products", show_products),
    "2": ("Categories", show_categories),
    "3": ("Carts", show_carts),
}


def main():
    print("Welcome to the Fake Store API Explorer!")

    while True:
        print("\nWhat would you like to view?")
        for key, (label, _) in MENU.items():
            print(f"{key}. {label}")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            sys.exit(0)

        if choice not in MENU:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        _, action = MENU[choice]
        action()


if __name__ == "__main__":
    main()

# The most difficult part was understanding how the FakeStore API's cart data is structured.
# Each cart contains a products list where each entry has both an item ID and a quantity, meaning
# unique items and total items are two different calculations from the same nested list. Getting
# that distinction right, while also handling network errors gracefully so the program never
# crashes on a bad connection, required careful attention to both the API schema and exception handling.