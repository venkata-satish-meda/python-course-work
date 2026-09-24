# Logic-building problems

numbers = [14, 7, 21, 9, 32, 18]
largest = numbers[0]
smallest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)

# Count even and odd values
even = odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)
