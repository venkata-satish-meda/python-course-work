number = int(input("Enter number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Palindrome" if original == reverse else "Not palindrome")
