# Day 10 - Recursive power
# This function calculates base raised to an exponent.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))
