import random

secret = random.randint(1, 10)
guess = int(input("Guess 1-10: "))

if guess == secret:
    print("Correct")
else:
    print("Try again. Number was:", secret)
