numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
