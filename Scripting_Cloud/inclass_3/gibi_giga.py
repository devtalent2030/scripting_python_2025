# A function that will convert from gibibytes to gigabytes (i.e. returning the converted value. and vice vesa)

GIBI_TO_GIGA_RATIO = 1_073_741_824 / 1_000_000_000

def gibi_to_giga(x: float) -> float:
    """
    Converts gibibytes to gigabytes.

    Args:
        x (float): The value in gibibytes.

    Returns:
        float: The equivalent value in gigabytes.
    """
    return x * GIBI_TO_GIGA_RATIO


def giga_to_gibi(x: float) -> float:
    """
    Converts gigabytes to gibibytes.

    Args:
        x (float): The value in gigabytes.

    Returns:
        float: The equivalent value in gibibytes.
    """
    return x / GIBI_TO_GIGA_RATIO


if __name__ == "__main__":
    print(gibi_to_giga(1))       # ≈ 1.073741824
    print(gibi_to_giga(2.5))     # ≈ 2.68435456
    print(giga_to_gibi(1))       # ≈ 0.9313225746
    print(giga_to_gibi(5))       # ≈ 4.656612873
