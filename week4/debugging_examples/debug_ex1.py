"""
This file contains example 1 of debugging in Python.
The code calculates the sum of a list of numbers.
The code is intended to sum the numbers in num_list and print the result.
However, it contains a bug that prevents it from working correctly.
The bug is that the variable 'sum' is a built-in function in Python, and using it as a variable name will cause issues.
The code should be fixed by renaming the variable 'sum' to something else, like 'total'.
"""

def add_numbers(num_list):
    # There is an issue with this code. Sum is a built-in function in Python.
    # sum will be renamed to total to avoid future issues and syntax issues
    
    # sum = 0
    total = 0
    
    for i in range(len(num_list)):
        # sum += num_list[i]
        total += num_list[i]
    
    return total

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]
    
    result = add_numbers(num_list)
    
    print("The sum is:", result)