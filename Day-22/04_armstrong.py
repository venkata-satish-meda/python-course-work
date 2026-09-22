number = int(input("Enter number: "))
digits = str(number)
total = sum(int(d) ** len(digits) for d in digits)

if total == number:
    print("Armstrong")
else:
    print("Not Armstrong")
