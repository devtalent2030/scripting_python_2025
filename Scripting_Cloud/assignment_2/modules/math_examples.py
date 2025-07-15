import math

"""
Function                 Use Case
                             
ceil()                   Always round up

floor()                  Always round down

fabs()                   Get positive difference only

isclose()                Floating point-safe comparisons


"""


# Example 1: math.ceil() – Round up to nearest integer
cost = 3.02
rounded = math.ceil(cost)
print("📈 Rounded up:", rounded)  # Output: 4

# Example 2: math.floor() – Round down to nearest integer
cost = 3.98
rounded = math.floor(cost)
print("📉 Rounded down:", rounded)  # Output: 3

# Example 3: math.fabs() – Absolute value (no negatives)
delta = -12.45
print("🧮 Absolute difference:", math.fabs(delta))  # Output: 12.45


# Example 4: math.isclose() – Compare floating point numbers safely
cost1 = 10.0000000001
cost2 = 10.0000000002

print("🧪 Are costs close enough?", math.isclose(cost1, cost2, rel_tol=1e-9))