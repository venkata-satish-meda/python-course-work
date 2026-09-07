# Day 7 - Global scope
# A variable created outside functions is in the global scope.

name = "Alex"

def show_name():
    print(name)

show_name()
print(name)
