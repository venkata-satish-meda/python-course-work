# Day 7 - global keyword
# global allows a function to change a global variable.

count = 1

def increase():
    global count
    count = count + 1

increase()
print(count)
