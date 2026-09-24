# Basic patterns using nested loops

rows = 5
for row in range(1, rows + 1):
    print("* " * row)

print()

for row in range(rows, 0, -1):
    print("* " * row)
