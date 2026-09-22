# Day 8 - Recursion introduction
# Recursion happens when a function calls itself.
# A base case is required to stop the recursion.

def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)
