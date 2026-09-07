# Day 9 - Scope rules
# Python commonly looks for names in this order:
# Local -> Enclosing -> Global -> Built-in.

name = "global"

def outer():
    name = "enclosing"

    def inner():
        print(name)

    inner()

outer()
