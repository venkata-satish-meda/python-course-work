# Variables change as a program runs

customer = "Ravi"
balance = 12500
print(customer, balance)

deposit = 2500
balance = balance + deposit
print("After deposit:", balance)

withdrawal = 1800
balance -= withdrawal
print("After withdrawal:", balance)

# Swapping two values
first_product = "Keyboard"
second_product = "Mouse"
first_product, second_product = second_product, first_product
print(first_product, second_product)
