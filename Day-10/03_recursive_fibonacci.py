# Day 10 - Recursive Fibonacci
# Fibonacci starts with 0 and 1.
# Each later value is the sum of the previous two.

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(6))
