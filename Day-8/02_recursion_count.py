# Day 8 - Recursive counting
# The function calls itself with a smaller value.

def count_up(number):
    if number > 5:
        return
    print(number)
    count_up(number + 1)

count_up(1)
