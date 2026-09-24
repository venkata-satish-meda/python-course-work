# Pattern problems with simple logic

rows = 5
for row in range(1, rows + 1):
    for column in range(1, rows + 1):
        if row == column or row + column == rows + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Multiplication table layout
for row in range(1, 4):
    for number in range(1, 6):
        print(row * number, end=" ")
    print()
