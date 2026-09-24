# Generators produce values one at a time

def transaction_amounts(transactions):
    for transaction in transactions:
        if transaction > 0:
            yield transaction

transactions = [1200, -50, 450, 0, 800]
for amount in transaction_amounts(transactions):
    print("Valid transaction:", amount)

def read_numbers(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

print(list(read_numbers(5)))
