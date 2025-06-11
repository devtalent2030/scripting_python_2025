# Example 3 - For Loops

number_string = ''

# This program will start a counter at 2 and increment by 2 until it reaches 30
# and print the numbers in a tab delimited format
for counter in range(2, 22, 2):
    number_string += str(counter) + ' '
    
print(number_string)