def find_max(num1, num2, num3):
    max_val = num1
    if num2 > max_val:
        max_val = num2
    if num3 > max_val:
        max_val = num3
    return max_val

if __name__ == "__main__":
    print(find_max(4, 10, 2))
    print(find_max(7, 3, 9))
    print(find_max(5, 5, 5))
    
    print(max(100, 200.90, 4000.2, 1000))