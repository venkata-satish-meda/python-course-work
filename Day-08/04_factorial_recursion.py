# Day 8 - Factorial with recursion
# factorial(n) means n multiplied by all positive numbers below it.

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))
