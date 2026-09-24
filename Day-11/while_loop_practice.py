# Process customer payments until the user chooses to stop

total = 0

while True:
    value = input("Enter payment (or done): ").strip().lower()
    if value == "done":
        break

    amount = float(value)
    if amount <= 0:
        print("Enter a positive amount.")
        continue

    total += amount
    print("Current total:", total)

print("Final collection:", total)
