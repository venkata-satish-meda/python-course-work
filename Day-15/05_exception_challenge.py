try:
    marks = int(input("Enter marks: "))
    if not 0 <= marks <= 100:
        raise ValueError
    print("Valid marks")
except ValueError:
    print("Invalid marks")
