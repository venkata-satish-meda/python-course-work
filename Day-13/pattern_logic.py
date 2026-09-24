# Pattern logic practice

rows = 5
for row in range(1, rows + 1):
    for column in range(1, rows + 1):
        if column <= row:
            print(column, end=" ")
        else:
            print("-", end=" ")
    print()

# Right aligned pattern
for row in range(1, rows + 1):
    print("  " * (rows - row) + "* " * row)
