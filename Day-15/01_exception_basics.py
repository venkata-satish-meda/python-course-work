try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
