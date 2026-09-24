# Different errors need different responses

values = ["100", "50", "abc", "25"]

for value in values:
    try:
        number = int(value)
        print(100 / number)
    except ValueError:
        print("Invalid number:", value)
    except ZeroDivisionError:
        print("Zero cannot be used:", value)
