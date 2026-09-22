# Day 9 - Enclosing scope
# A nested function can read a variable from its enclosing function.

def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    inner()

outer()
