# Lambda with built-in functions

prices = [1200, 450, 3200, 800]
print("Sorted:", sorted(prices))

products = [
    ("Keyboard", 1200),
    ("Monitor", 8500),
    ("Mouse", 650)
]

by_price = sorted(products, key=lambda item: item[1])
print(by_price)

names = ["ravi", "PRIYA", "kiran"]
print(sorted(names, key=lambda name: name.lower()))
