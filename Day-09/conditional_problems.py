# Practical conditional problems

salary = 42000
years = 4

if years >= 5:
    bonus = salary * 0.20
elif years >= 3:
    bonus = salary * 0.12
else:
    bonus = salary * 0.05

print("Bonus:", bonus)

# Electricity bill slab
units = 240
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5

print("Electricity bill:", bill)
