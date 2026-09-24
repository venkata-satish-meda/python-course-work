# Conditional practice

amount = 5200
member = True

if member and amount >= 3000:
    discount = 15
elif amount >= 3000:
    discount = 10
else:
    discount = 0

final_amount = amount - amount * discount / 100
print("Discount:", discount, "%")
print("Final amount:", final_amount)

# Scholarship screening
marks = 86
attendance = 91
family_income = 180000

if marks >= 80 and attendance >= 85 and family_income <= 250000:
    print("Eligible for scholarship screening")
else:
    print("Not eligible")
