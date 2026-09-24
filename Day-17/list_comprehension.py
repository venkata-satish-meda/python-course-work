# List comprehensions

numbers = [12, 15, 18, 21, 24, 27]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

names = ["ravi", "priya", "kiran"]
upper_names = [name.upper() for name in names]
print(upper_names)

prices = [1000, 1500, 2000]
discounted = [price * 0.9 for price in prices]
print(discounted)
