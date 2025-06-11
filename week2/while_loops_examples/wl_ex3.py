# Example 3 - While Loops

# This program will keep asking the user for a number till the user enters 0,
# then will sum all numbers.
# The program will also count how many numbers were entered.

# Initialize variables
sum = 0
count = 0
number = 1

# Loop until the user enters 0
while number != 5:
    # Ask the user for a number
    number = int(input("Enter a number (0 to stop): "))
    
    # If the number is not 0, add it to the sum and increment the count
    if number != 5:
        sum += number
        count += 1
        
# Print the results
print(f'You entered { count } numbers.')
print(f'The sum of the numbers is { sum }.')