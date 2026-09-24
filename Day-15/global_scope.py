# Reading and updating a global variable

tax_rate = 18

def show_tax():
    print("Current tax rate:", tax_rate)

show_tax()

counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()
print("Counter:", counter)
