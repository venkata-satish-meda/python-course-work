# Day 10 - Scope with recursion
# Each function call has its own local variables.

def countdown(number):
    current = number

    if current == 0:
        return

    print("Current:", current)
    countdown(current - 1)

countdown(5)
