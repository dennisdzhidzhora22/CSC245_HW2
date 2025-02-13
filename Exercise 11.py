# Guess the number game
import random

n = random.randint(1, 20)
print("There is a random number between 1 and 20, inclusive. Try to guess what it is: ")
guess = -1

while guess != n:
    guess = int(input("Your guess: "))
    if guess < n:
        print("That number is too low. Try again")
    if guess > n:
        print("That number is too high. Try again")

print(f"Correct, the number was {n}.")