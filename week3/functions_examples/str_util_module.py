"""
This module provides utility functions for string manipulation.
This module will be used by str_main.py
"""

def concat_str(a: str, b: str) -> str:
    """
    Concatenates two strings.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return a + b

def concat_many(*args: str) -> str:
    """
    Concatenates multiple strings. Example of a function that takes a variable number of arguments.

    Args:
        *args (str): A variable number of strings to be concatenated.

    Returns:
        str: The concatenated string.
    """
    return ''.join(args)

def concat_list(a: list) -> str:
    """
    Concatenates all strings in a list.

    Args:
        a (list): A list of strings.

    Returns:
        str: The concatenated string.
    """
    return ''.join(a)

def concat_list_with_sep(a: list, sep: str) -> str:
    """
    Concatenates all strings in a list with a custom defined separator.

    Args:
        a (list): A list of strings.
        sep (str): The separator string.

    Returns:
        str: The concatenated string with the separator.
    """
    return sep.join(a)