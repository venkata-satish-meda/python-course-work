# Functions make repeated business logic reusable

def calculate_discount(amount, percent):
    return amount * percent / 100

def final_amount(amount, percent):
    discount = calculate_discount(amount, percent)
    return amount - discount

bill = 4500
print("Discount:", calculate_discount(bill, 12))
print("Final amount:", final_amount(bill, 12))

def is_adult(age):
    return age >= 18

print(is_adult(21))
