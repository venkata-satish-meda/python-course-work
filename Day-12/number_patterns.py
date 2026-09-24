# Number patterns

for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

print()

for row in range(1, 6):
    for number in range(row):
        print(row, end=" ")
    print()
