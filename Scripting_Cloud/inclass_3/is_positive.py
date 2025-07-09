# A function that will return True if its parameter is a positive number (i.e. float), and return False otherwise.


def is_positive(x: float) -> bool:
    """
    Checks whether a given number is positive.

    Args:
        x (float): A number to be checked.

    Returns:
        bool: True if x is greater than 0, False otherwise.
    """
    return x > 0


if __name__ == "__main__":
    print(is_positive(1))    # True
    print(is_positive(0))    # False
    print(is_positive(-5))   # False
    print(is_positive(2.5))  # True
    print(is_positive(-0.1)) # False
