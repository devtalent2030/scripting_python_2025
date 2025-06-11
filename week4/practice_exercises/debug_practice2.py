"""
Fix the syntax in the condition.
Recognize range(10) does not include 10.
"""

if __name__ == "__main__":
    
    for i in range(10):
        if i % 2 == 0:
            print(f"{i} is even")
