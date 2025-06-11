"""
This is example 2 of debugging in Python.
The code is intended to calculate the average of a list of numbers.
However, it contains a bug that prevents it from working correctly.
The bug is that the variable 'average' is not defined before it is used.
"""

def calculate_average(num_list):
    # There is an issue with this code. Average is not defined before it is used.
    # average will be initialized to 0 to avoid future issues and syntax issues
    
    
    average = 0 # Uncomment this line to mitigate the issue
    total = 0
    count = len(num_list)
    
    for i in range(count):
        total += num_list[i] # Add a breakpoint here to view the value of total
    
    # average = total / count
    average = total / count if count > 0 else 0
    
    return average

if __name__ == "__main__":
    num_list = [10, 20, 30, 40, 50]
    
    result = calculate_average(num_list)
    
    print(f"The average is: {result:.2f}")  # Print the result with two decimal places

# Note: The code has been modified to include a check for division by zero