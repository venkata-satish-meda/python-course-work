# Type conversion in practical input handling

age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
phone = input("Enter your phone number: ")

print("Age next year:", age + 1)
print("Height:", height, "cm")
print("Phone stored as:", str(phone))

# Convert a mark from text to a number
mark_text = "87"
mark = int(mark_text)
print("Mark + 5:", mark + 5)

# Convert a list of numeric strings
prices = ["120", "250", "80"]
numeric_prices = [int(price) for price in prices]
print("Total:", sum(numeric_prices))
