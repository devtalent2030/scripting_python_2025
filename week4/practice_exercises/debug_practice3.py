def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("The total is: " + str(sum_list(nums)))
