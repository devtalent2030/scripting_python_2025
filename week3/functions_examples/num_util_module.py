"""
This module contains utility functions for number manipulation.
This module will be used by num_main.py
"""

def add_many(*args: int) -> int:
    """
    Adds multiple integers. Example of a function that takes a variable number of arguments.

    Args:
        *args (int): A variable number of integers to be added.

    Returns:
        int: The sum of the integers.
    """
    return sum(args)

def add_func(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b

def sub_func(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of the subtraction.
    """
    return a - b

def add_list(a: list) -> int:
    """
    Adds all integers in a list.

    Args:
        a (list): A list of integers.

    Returns:
        int: The sum of the integers in the list.
    """
    return sum(a)

def sub_list(a: list) -> int:
    """
    Subtracts all integers in a list from the first integer sorted in descending order.

    Args:
        a (list): A list of integers.

    Returns:
        int: The result of the subtraction.
    """
    a.sort(reverse=True)
    
    return a[0] - sum(a[1:])


