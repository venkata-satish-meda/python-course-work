# Day 10 - Recursion practice
# Use a base case and a recursive case.

def print_numbers(number):
    if number == 0:
        return
    print_numbers(number - 1)
    print(number)

print_numbers(5)
