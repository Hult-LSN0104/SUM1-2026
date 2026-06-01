"""
Book Class Starter File
=======================
In this exercise, you will build a simple Book class that tracks
book information and whether it is checked out or available.

Complete each TODO section below. Do NOT change any method names or
the test function at the bottom.
"""


class Book:
    """Represents a book in a library system."""

    def __init__(self, title, author, pages):
        """
        TODO 1 – Initialize the book's attributes.

        Parameters:
            title  (str): The title of the book.
            author (str): The author's name.
            pages  (int): The number of pages.

        Steps:
            1. Remove the `pass` statement below.
            2. Use self.attribute_name = value to store each parameter.
            3. Also create self.is_available and set it to True.

        Example:
            self.title = title
        """
        # ADD YOUR CODE HERE
        pass

    def checkout(self):
        """
        TODO 2 – Check out the book if it is available.

        Returns:
            True  if the book was successfully checked out.
            False if the book was already checked out.

        Steps:
            1. Remove the `pass` statement below.
            2. Use an if-else statement to check self.is_available.
            3. If available:  set self.is_available = False, return True.
            4. If not available: return False.
        """
        # ADD YOUR CODE HERE
        pass

    def return_book(self):
        """
        TODO 3 – Return the book (mark it as available again).

        Returns:
            True always, to indicate the return was successful.

        Steps:
            1. Remove the `pass` statement below.
            2. Set self.is_available to True.
            3. Return True.

        Note: You do NOT need to check any conditions here.
        """
        # ADD YOUR CODE HERE
        pass

    def get_info(self):
        """
        TODO 4 – Build and return a descriptive string about the book.

        Returns:
            A formatted string with the book's details.

        Steps:
            1. Remove the `pass` statement below.
            2. Convert self.is_available to the word "Available" or
               "Not Available".
            3. Use an f-string to combine all attributes.

        Expected format:
            "The Hobbit by J.R.R. Tolkien (295 pages) - Available"
        """
        # ADD YOUR CODE HERE
        pass


# ---------------------------------------------------------------------------
# Test function – DO NOT modify anything below this line
# ---------------------------------------------------------------------------

def test_book_class():
    """Runs a series of tests on your Book class and prints the results."""

    print("=== Testing Book Class ===")
    title  = input("Enter the book name: ")
    author = input("Enter the author name: ")
    pages  = int(input("Enter the number of pages: "))

    book = Book(title, author, pages)

    # Test 1 – Initial state
    print("\nTest 1: Initial state")
    print("Initial book info:", book.get_info())
    # Expected: <title> by <author> (<pages> pages) - Available

    # Test 2 – First checkout
    print("\nTest 2: First checkout attempt")
    result = book.checkout()
    print("Checkout successful?", result)           # Expected: True
    print("After checkout:", book.get_info())
    # Expected: <title> by <author> (<pages> pages) - Not Available

    # Test 3 – Second checkout (should fail)
    print("\nTest 3: Second checkout attempt")
    result2 = book.checkout()
    print("Second checkout successful?", result2)   # Expected: False

    # Test 4 – Return
    print("\nTest 4: Return book")
    result3 = book.return_book()
    print("Return successful?", result3)            # Expected: True
    print("After return:", book.get_info())
    # Expected: <title> by <author> (<pages> pages) - Available


# Run the tests automatically when this file is executed
if __name__ == "__main__":
    test_book_class()
