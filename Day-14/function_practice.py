# Function practice: invoice calculation

def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100

def generate_invoice(items, tax_rate=18):
    subtotal = sum(price * quantity for price, quantity in items)
    tax = calculate_tax(subtotal, tax_rate)
    total = subtotal + tax
    return subtotal, tax, total

items = [(1200, 1), (650, 2), (300, 3)]
subtotal, tax, total = generate_invoice(items)

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)

def is_even(number):
    return number % 2 == 0

print("Even:", is_even(48))
