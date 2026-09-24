# Parameters and return values

def calculate_salary(basic, allowance=0, deduction=0):
    return basic + allowance - deduction

print(calculate_salary(30000))
print(calculate_salary(30000, 5000, 1200))

def create_order_summary(order_id, amount, status="Pending"):
    return f"{order_id} | ₹{amount:.2f} | {status}"

print(create_order_summary("ORD501", 1899, "Paid"))
