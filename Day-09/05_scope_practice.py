# Day 9 - Scope practice
# Compare local, enclosing, and global variables.

message = "global"

def outer():
    message = "enclosing"

    def inner():
        message = "local"
        print(message)

    inner()
    print(message)

outer()
print(message)
