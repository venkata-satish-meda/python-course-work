# Set comprehensions

numbers = [10, 11, 10, 12, 13, 11, 14]
squares = {number * number for number in numbers}
print(squares)

cities = ["Hyderabad", "hyderabad", "Chennai", "Pune"]
normalized = {city.lower() for city in cities}
print(normalized)
