# Recursion: a function calls itself with a smaller problem

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print("5! =", factorial(5))

def sum_to_n(number):
    if number == 0:
        return 0
    return number + sum_to_n(number - 1)

print("Sum:", sum_to_n(5))
