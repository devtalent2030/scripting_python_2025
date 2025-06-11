""" def function_main():
    while True:
        try:
            fahrenheit = float(input("Enter Fahrenheit temperature: "))
            celcius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f} Fahrenheit is  {celcius:.2f}  celcius")
            break
        except ValueError:
            print("please enter a number !")

function_main()   """


sum = 0

for counter in range(6, 8):
    sum += counter

    print(sum)