"""
Name: Talent Nyota
Date: 12-06-2025
Program Description: Mid-term-test
"""

# constants

NUMBER_OF_DEPARTMENTS = 3
MAXIMUM_TOTAL_USERS = 32

# input

number_users_first_department = int(input("please enter the number of users in the first department: "))
number_users_second_department = int(input("please enter the number of users in the second department: "))


user_entred = number_users_first_department + number_users_second_department
remaining_users = MAXIMUM_TOTAL_USERS - user_entred

if number_users_first_department > MAXIMUM_TOTAL_USERS:
    print("You have exceeded the maximum allowable users.")
elif number_users_second_department > MAXIMUM_TOTAL_USERS:
    print("You have exceeded the maximum allowable users.")
elif number_users_first_department == MAXIMUM_TOTAL_USERS:
    print("There are no additional users allowed")
elif number_users_second_department == MAXIMUM_TOTAL_USERS:
    print("There are no additional users allowed")
else:
    print(f"There are {remaining_users} users still available.")

print(f"Department 1 users: {number_users_first_department}")
print(f"Department 2 users: {number_users_second_department}")

print("please enter enter return to Exit the proogram")

