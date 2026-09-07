# Day 9 - nonlocal
# nonlocal lets a nested function change a variable in its enclosing function.

def counter():
    count = 0

    def increase():
        nonlocal count
        count = count + 1
        print(count)

    increase()
    increase()

counter()
