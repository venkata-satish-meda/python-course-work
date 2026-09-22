while True:
    try:
        age = int(input("Enter age: "))
        if age >= 0:
            break
        print("Age cannot be negative")
    except ValueError:
        print("Enter a number")

print("Age:", age)
