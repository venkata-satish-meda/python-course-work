# This file demonstrates the idea of a custom module.
# Save the following in a file named shop_utils.py if you want
# to import it from another Python file.

def calculate_total(price, quantity):
    return price * quantity

def apply_discount(amount, percent):
    return amount - (amount * percent / 100)

if __name__ == "__main__":
    total = calculate_total(1200, 2)
    print(apply_discount(total, 10))
