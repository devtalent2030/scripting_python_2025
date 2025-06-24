"""
Name: Talent Nyota
Date: 22-05-2025
Program Description:
This script analyzes a number to determine:
1. Whether it is a prime number
2. What its prime divisors are (if not prime)
3. The nearest prime number before it
4. The nearest prime number after it

This script was written after a full mathematical breakdown and manual
exploration using examples like 143 and 60. The logic reflects the same
steps used in RSA encryption: multiplying large primes and understanding
their properties. All functions were built from scratch to reflect my
own understanding of prime checking, factorization, and number theory.
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.
    
    Example:
        is_prime(7) → True
        is_prime(12) → False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_divisors(n):
    """
    Find all prime divisors of a number.

    Parameters:
        n (int): The number to factor.

    Returns:
        list[int]: List of prime numbers that divide n.

    Example:
        prime_divisors(60) → [2, 3, 5]
    """
    divisors = []
    for d in range(2, n + 1):
        if n % d == 0 and is_prime(d):
            divisors.append(d)
    return divisors


def nearest_prime_before(n):
    """
    Find the nearest prime number smaller than n.

    Parameters:
        n (int): The reference number.

    Returns:
        int or None: The nearest smaller prime, or None if not found.

    Example:
        nearest_prime_before(143) → 139
    """
    candidate = n - 1
    while candidate > 1:
        if is_prime(candidate):
            return candidate
        candidate -= 1
    return None


def nearest_prime_after(n):
    """
    Find the nearest prime number larger than n.

    Parameters:
        n (int): The reference number.

    Returns:
        int: The nearest larger prime.

    Example:
        nearest_prime_after(143) → 149
    """
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


def analyze_number(n):
    """
    Analyze a number and print its prime-related properties.

    Parameters:
        n (int): The number to analyze.

    Output:
        Prints the result to the screen.

    Example:
        analyze_number(143)
    """
    print(f"\nAnalyzing number: {n}")

    before = nearest_prime_before(n)
    after = nearest_prime_after(n)

    print(f"The prime number before {n} is {before}.")

    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        divs = prime_divisors(n)
        print(f"{n} is not prime. Its factors are {', '.join(map(str, divs))}.")

    print(f"The prime number after {n} is {after}.")


if __name__ == "__main__":
    # Prompt user for input until valid positive whole number is entered
    while True:
        user_input = input("Please enter a positive whole number to check: ")
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                analyze_number(number)
                break
            else:
                print("That is not a positive whole number. Try again.\n")
        else:
            print("That is not a positive whole number. Try again.\n")

    input("\nPress Enter to exit the program...")
