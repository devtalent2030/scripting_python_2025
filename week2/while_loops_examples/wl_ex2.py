# Example 2 - While Loops

month_counter = 1
months_to_invest = 24
monthly_interest_rate = 0.01
monthly_investment = 100
future_value = 0

# while there are months to invest
while month_counter <= months_to_invest:
    # calculate the future value
    future_value = (future_value + monthly_investment) * (1 + monthly_interest_rate)
    
    # increment the month counter
    month_counter += 1
    
    # print future value for each iteration
    print(f'Current future value: {future_value:.2f}')
    
# print the future value
# print(f'Future value: ${future_value:.2f}')