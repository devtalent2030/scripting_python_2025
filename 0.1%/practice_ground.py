


# TUPLES

"""i = (10, 20, 30, 40, 40)

dir(i)

print(dir(i))


s = i.__add__((300, 500))


print(s)

print(i) 



# List


import sys, gc
lst = []
sizes = []




for n in range(50):
    lst.append(n)
    sizes.append(sys.getsizeof(lst))
    append_1 = list.append([51])
print(sizes[:10], "...")          # watch size plateau then jump
print(lst[:10])
print(append_1)



if (line := input("Type: ")) != "":
    print("You typed:", line)


    print(__name__)  # Prints: __main__ (when run directly)
print(dir(__name__))
           
 
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    

def prime_divisors(n):
    divisors = []
    for d in range(2, n + 1):
        if n % d == 0 and is_prime(d):
            divisors.append(d)
    return divisors


def nearest_prime_before(n):
    candidate = n - 1
    while n > 1:
        if  is_prime(candidate):
            return candidate
        candidate -= 1
    return None

   

"""

import requests

print(dir(requests))  # 🔍 See all attributes inside the requests module
