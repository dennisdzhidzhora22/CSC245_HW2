# FizzBuzz
for i in range(1, 101):
    s = ""

    if i % 3 == 0:
        s = s + "Fizz"
    if i % 5 == 0:
        s = s + "Buzz"

    if len(s) == 0:
        print(i)
    else:
        print(s)