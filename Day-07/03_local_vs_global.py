# Day 7 - Local vs global
# A local variable can have the same name as a global variable.
# They are separate variables.

name = "Global Alex"

def show_name():
    name = "Local Alex"
    print(name)

show_name()
print(name)
