# Number problem practice

number = 153
original = number
total = 0

while number > 0:
    digit = number % 10
    total += digit ** 3
    number //= 10

print("Armstrong number:", total == original)

# Find the sum of digits
number = 5824
digit_sum = 0
while number:
    digit_sum += number % 10
    number //= 10

print("Digit sum:", digit_sum)
