# Example 1 - Iteration through a list

string_list = ['Bob', 'Alice', 'Charlie', 'Dave', 'Eve', 'Harry']

# Print each name in the list
for name in string_list:
    print(name)

print('\n', '*' * 20, '\n')
 
# Print each name in the list with its index
for index in range(len(string_list)):
    print(f'Index: {index}, Name: {string_list[index]}')

print(string_list[3])