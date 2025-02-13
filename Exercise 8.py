# Factorial of a number
n = int(input("Enter a number to find the factorial of: "))

isNegative = False
if n < 0:
    print("Please enter a non-negative integer.")
    isNegative = True

factorial = 1

if not isNegative:
    while n > 1:
        factorial *= n
        n -= 1

    print("The factorial of this number is " + str(factorial))