try:
    number = int(input())
except ValueError:
    print("Invalid number")
else:
    print("Number:", number)
finally:
    print("Program finished")
