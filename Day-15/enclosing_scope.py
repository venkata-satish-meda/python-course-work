# Enclosing scope and nonlocal

def create_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase

counter = create_counter()
print(counter())
print(counter())
print(counter())

# Another practical example
def create_discount_calculator(rate):
    def calculate(amount):
        return amount * rate / 100
    return calculate

festival_discount = create_discount_calculator(15)
print("Discount:", festival_discount(3000))
