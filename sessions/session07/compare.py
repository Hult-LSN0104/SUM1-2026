# compare.py

import time
import random
import os
from sort import SortingAlgorithms

def measure_sort_time(sort_func, arr):
    """Measure the time taken by a sorting algorithm to sort an array."""
    arr_copy = arr.copy()  # Create a copy to avoid modifying original array
    start_time = time.time()
    sorted_arr = sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time, sorted_arr

def compare_sorting_algorithms(arr_size=1000):
    """Compare the performance of different sorting algorithms."""

    # Files are expected in a folder called 'files_to_test' next to this script
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files_to_test")

    def read_array_from_file(filename):
        """Read array from a file. Supports txt and csv formats."""
        filepath = os.path.join(base_dir, filename)
        try:
            with open(filepath, 'r') as file:
                if filename.endswith('.csv'):
                    import csv
                    reader = csv.reader(file)
                    return [int(x.strip()) for x in next(reader) if x.strip()]
                else:
                    content = file.read()
                    if '\n' in content:
                        return [int(x.strip()) for x in content.split('\n') if x.strip()]
                    else:
                        return [int(x.strip()) for x in content.split() if x.strip()]
        except FileNotFoundError:
            print(f"Warning: {filepath} not found. Using default random array.")
            return [random.randint(1, 1000) for _ in range(arr_size)]
        except (ValueError, Exception) as e:
            print(f"Error reading {filepath}: {e}. Using default random array.")
            return [random.randint(1, 1000) for _ in range(arr_size)]

    # Test cases — put your .txt files in the files_to_test folder
    test_arrays = {
        "Random":         read_array_from_file("random10000.txt"),
        "Already Sorted": read_array_from_file("sorted10000.txt"),
        "Reverse Sorted": read_array_from_file("reversed5000.txt"),
    }

    # Dictionary to store all sorting functions
    sorting_functions = {
        "Sort 1": SortingAlgorithms().sort_one,
        "Sort 2": SortingAlgorithms().sort_two,
        "Sort 3": SortingAlgorithms().sort_three,
    }

    # Compare each sorting algorithm with each test case
    results = {}
    for array_type, test_arr in test_arrays.items():
        print(f"\nTesting with {array_type} array:")
        print("-" * 40)

        for sort_name, sort_func in sorting_functions.items():
            time_taken, _ = measure_sort_time(sort_func, test_arr)
            print(f"{sort_name}: {time_taken:.4f} seconds")

            if array_type not in results:
                results[array_type] = {}
            results[array_type][sort_name] = time_taken

    return results

def main():
    results = compare_sorting_algorithms()
    print("\nResults:")
    print("-" * 40)
    for array_type, timing_data in results.items():
        print(f"\n{array_type} array:")
        for sort_name, time_taken in timing_data.items():
            print(f"{sort_name}: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main()
