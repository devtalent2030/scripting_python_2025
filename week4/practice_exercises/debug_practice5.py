def countdown(n):
    while n >= 0:
        print(n)
        # n = n - 1
        n -= 1
    print("Blast off!")

if __name__ == "__main__":
    countdown(8)
