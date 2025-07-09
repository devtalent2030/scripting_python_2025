# A function that will return True if its parameter is a power of 2 (e.g. 2, 4, 8, 16, 32), and return False otherwise. 


def is_power_of_two(x: float) -> bool:
    """
    Checks if a number is a power of two.

    Args:
        x (float): The number to check.

    Returns:
        bool: True if x is a power of 2, False otherwise.
    """
    return x > 0 and (x & (x - 1)) == 0


if __name__ == "__main__":
    print(is_power_of_two(1))   # True (2^0)
    print(is_power_of_two(2))   # True (2^1)
    print(is_power_of_two(3))   # False
    print(is_power_of_two(8))   # True (2^3)
    print(is_power_of_two(10))  # False
