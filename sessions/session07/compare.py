# main.py

import time
import random
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
    def read_array_from_file(filename):
        """Read array from a file. Supports txt and csv formats."""
        try:
            with open(filename, 'r') as file:
                if filename.endswith('.csv'):
                    # For CSV files, use csv module
                    import csv
                    reader = csv.reader(file)
                    # Read first row and convert to integers
                    return [int(x.strip()) for x in next(reader) if x.strip()]
                else:
                    # For txt files, assume one number per line or space-separated
                    content = file.read()
                    if '\n' in content:
                        # One number per line
                        return [int(x.strip()) for x in content.split('\n') if x.strip()]
                    else:
                        # Space-separated numbers
                        return [int(x.strip()) for x in content.split() if x.strip()]
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Using default array.")
            return [random.randint(1, 1000) for _ in range(arr_size)]
        except (ValueError, csv.Error) as e:
            print(f"Error reading {filename}: {e}. Using default array.")
            return [random.randint(1, 1000) for _ in range(arr_size)]

    # Test cases to try - read from files with fallback to generated arrays
    test_arrays = {
        "Random": read_array_from_file("/Users/ctoddlombardo/Dropbox/_Hult/Courses/CM-3/code/files_to_test/random50000.txt"),
        "Already Sorted": read_array_from_file("/Users/ctoddlombardo/Dropbox/_Hult/Courses/CM-3/code/files_to_test/sorted50000.txt"),
        "Reverse Sorted": read_array_from_file("/Users/ctoddlombardo/Dropbox/_Hult/Courses/CM-3/code/files_to_test/reversed50000.txt")
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
            
            # Store results for later analysis
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
