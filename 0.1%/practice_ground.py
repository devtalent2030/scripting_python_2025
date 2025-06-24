


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



"""

import dis

def check_grade(grade):
    if grade >= 50:
        return "Pass"
    else:
        return "Fail"

dis.dis(check_grade)