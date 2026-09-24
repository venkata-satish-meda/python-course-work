# Lambda functions for small one-line operations

square = lambda number: number * number
print(square(8))

add_tax = lambda amount: amount * 1.18
print(round(add_tax(1000), 2))

is_adult = lambda age: age >= 18
print(is_adult(21))
