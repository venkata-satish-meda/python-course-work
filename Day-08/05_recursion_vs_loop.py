# Day 8 - Recursion vs loop
# Both approaches can repeat work.
# This example shows the same counting idea in two ways.

def recursive_count(number):
    if number == 0:
        return
    recursive_count(number - 1)
    print(number)

recursive_count(5)

print("Loop:")

for number in range(1, 6):
    print(number)
