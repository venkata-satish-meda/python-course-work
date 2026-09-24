# Skip unwanted records

transactions = [1200, 0, 450, 0, 890]
total = 0

for amount in transactions:
    if amount == 0:
        continue
    total += amount

print("Total valid transactions:", total)

# Skip inactive employees
employees = [
    ("Ravi", True),
    ("Priya", False),
    ("Kiran", True)
]

for name, active in employees:
    if not active:
        continue
    print("Send report to:", name)
