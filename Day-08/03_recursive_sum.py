# Day 8 - Recursive sum
# Each call adds one number and asks the next call for the rest.

def total(number):
    if number == 0:
        return 0
    return number + total(number - 1)

print(total(5))
