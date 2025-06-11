'''
Author: Sohaib
'''

# Import the mult_function module
import mult_function

# This function takes a list of numbers and returns their sum
def add(a:list) -> int:
    """
    This is an example of a docstring.
    It can be used to explain the purpose of the function.
    -> represents what data type the function will return
    Args:
        a (list): A list of numbers to be summed.
    Returns:
        int: The sum of the numbers in the list.
    Example:
        >>> add([1, 2, 3])
        6
    """
    # Initialize the sum variable to 0
    sum = 0
    
    # Iterate through each number in the list and add it to the sum
    for each_num in a:
        # Add the current number to the sum
        sum += each_num
    
    # Return the final sum
    # The return statement is used to return a value from the function
    return sum

# Initialize 2 strings and join them
# The join method is used to concatenate strings
some_str = "Sohaib "
some_other_str = "Mohiuddin"

# The join method is called on some_str and takes some_other_str as an argument
some_str.join(some_other_str)

# Print the result of the add function
print(add([1, 2, 3]))

# Print the result of the mult2 function from the mult_function module
print(mult_function.mult2(35, 35, 35))