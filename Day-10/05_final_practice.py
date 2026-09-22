# Day 10 - Final practice
# This combines functions, recursion, parameters, return, and local scope.

def sum_to(number):
    # number is local to each function call.
    if number == 0:
        return 0

    return number + sum_to(number - 1)

result = sum_to(10)
print("Sum:", result)
