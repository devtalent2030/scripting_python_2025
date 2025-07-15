import datetime


"""
Function                               Use Case

datetime.today()                       Get current date

strptime()                             Convert string to date

strftime()                             Convert date to readable string

timedelta                              Calculate difference between two dates

"""



# Example 1: Get today’s date
today = datetime.date.today()
print("📆 Today's date:", today)

# Example 2: Convert string to date object
date_str = "2023-10-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
print("📅 Parsed date:", date_obj)

# Example 3: Compare two dates

d1 = datetime.datetime.strptime("2023-10-01", "%Y-%m-%d")
d2 =  datetime.datetime.strptime("2023-10-03", "%Y-%m-%d")

delta = d2 - d1
print("🕓 Days between:", delta.days)  # Output: 2


# Example 4: Format a date object to string
now = datetime.datetime.now()
print("🕰️ Pretty format:", now.strftime("%A %d %B %Y"))  # Output: Monday 01 January 2023