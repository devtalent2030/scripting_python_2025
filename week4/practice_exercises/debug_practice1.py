"""
Identify syntax errors in the elif and else blocks.
Understand boolean logic in conditions.
"""

def greet_user(hour):
    if (hour < 12):
        print("Good morning")
    elif (hour >= 12 and hour < 18):
        print("Good afternoon")
    else:
        print("Good evening")

if __name__ == "__main__":
    greet_user(18)
