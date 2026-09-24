# Combine file handling and exception handling

filename = "accounts.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        amount = float(line.strip())
        total += amount

    print("Total account balance:", total)

except FileNotFoundError:
    print("Account file is missing.")
except ValueError:
    print("One of the records is not a valid amount.")
