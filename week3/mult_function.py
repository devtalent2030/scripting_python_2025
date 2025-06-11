"""
This is an example of a module
This module contains two functions: mult and mult2.
The mult function takes two integers as arguments and returns their product.
The mult2 function takes three integers as arguments and returns their product.
"""

def mult(a:int, b:int) -> int:
    """
    This function will take 2 integers as input

    Args:
        a (int): first integer input
        b (int): second integer input

    Returns:
        int: The product or multiplication of the 2 integers
    """
    return a * b

def mult2(a:int, b:int, c:int) -> int:
    """
    This function will take 3 integers as input

    Args:
        a (int): first integer input
        b (int): second integer input
        c (int): third integer input

    Returns:
        int: The product or multiplication of the 3 integers
    """
    return a * b * c