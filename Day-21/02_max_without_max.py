numbers = [12, 45, 7, 89, 23]
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest)
