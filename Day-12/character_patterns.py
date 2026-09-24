# Character patterns

for row in range(1, 6):
    for column in range(row):
        print(chr(64 + row), end=" ")
    print()

print()

letters = "ABCDE"
for row in range(1, 6):
    print(" ".join(letters[:row]))
