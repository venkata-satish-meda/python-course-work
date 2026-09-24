# Star patterns used for nested-loop practice

rows = 5

for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    stars = "* " * row
    print(spaces + stars)

print()

for row in range(rows, 0, -1):
    print("* " * row)
