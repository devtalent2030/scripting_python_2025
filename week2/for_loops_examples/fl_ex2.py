# Example 2 - For Loops

month_counter = 1
months_to_invest = 24
monthly_interest_rate = 0.01
monthly_investment = 100
future_value = 0

# for each month in the range of months to invest
for month_counter in range(1, months_to_invest + 1):
    # calculate the future value
    future_value = (future_value + monthly_investment) * (1 + monthly_interest_rate)
    
# print the future value
print(f'Future value: ${future_value:.2f}')