# String formatting for reports

name = "Suresh"
salary = 38500
attendance = 91.456

print(f"Employee: {name}")
print(f"Salary: ₹{salary:,.2f}")
print(f"Attendance: {attendance:.1f}%")

product = "Laptop"
price = 54999
quantity = 2
print(f"{product:<12} {quantity:>3} x ₹{price:,.2f}")

total = price * quantity
print(f"Total amount: ₹{total:,.2f}")
