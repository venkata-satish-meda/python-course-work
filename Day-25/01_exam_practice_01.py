# Find the second largest unique number.

numbers = list(map(int, input("Enter numbers: ").split()))
unique = sorted(set(numbers))

if len(unique) < 2:
    print("No second largest")
else:
    print(unique[-2])
