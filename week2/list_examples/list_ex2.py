# Example 2 - Iteration through a List

# I want to find the average of all the grades in the grades list
sum = 0
grades = [80.0, 90.0, 100.0, 40.0, 25.55, 78.90]

# Incorrect way to calculate sum
# sum = grades[0] + grades[1] + grades[2]

# Correct way to calculate sum
for grade in grades:
    sum += grade
    
print(f'Sum = {sum:.2f}')
print(f'Length of grades list = { len(grades) }')
print(f'Average of all grades = {(sum / len(grades)):.2f}')