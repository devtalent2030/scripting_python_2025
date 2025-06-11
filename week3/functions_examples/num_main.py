"""
This script will utilize the num_util_module.
"""

# Import the num_util_module
import num_util_module as num_util

if __name__ == "__main__":
    # Example usage of the functions in num_util_module
    num1 = 10
    num2 = 5
    
    # Add two integers
    result = num_util.add_func(num1, num2)
    print(f"Addition of {num1} and {num2}: {result}")
    
    # Subtract two integers
    result = num_util.sub_func(num1, num2)
    print(f"Subtraction of {num1} and {num2}: {result}")
    
    # Add multiple integers
    result = num_util.add_many(1, 2, 3, 4, 5)
    print(f"Addition of multiple integers: {result}")
    
    # Subtract a list of integers
    num_list = [5, 2, 20, 10, 3]
    result = num_util.sub_list(num_list)
    print(f"Subtraction of list: {result}")