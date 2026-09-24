# Handle invalid user input

try:
    amount = float(input("Enter amount: "))
    quantity = int(input("Enter quantity: "))
    print("Total:", amount * quantity)
except ValueError:
    print("Please enter valid numbers.")

try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter an integer.")
