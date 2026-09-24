# Dictionary comprehensions

numbers = range(1, 6)
squares = {number: number * number for number in numbers}
print(squares)

products = ["keyboard", "mouse", "monitor"]
prices = [1200, 650, 8500]
catalog = {product: price for product, price in zip(products, prices)}
print(catalog)

high_value = {
    product: price
    for product, price in catalog.items()
    if price >= 1000
}
print(high_value)
