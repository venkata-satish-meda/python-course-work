# Variable practice using realistic values

employee_name = input("Employee name: ")
monthly_salary = float(input("Monthly salary: "))
working_days = int(input("Working days: "))
leave_days = int(input("Leave days: "))

paid_days = working_days - leave_days
daily_salary = monthly_salary / working_days
estimated_pay = daily_salary * paid_days

print("Employee:", employee_name)
print("Paid days:", paid_days)
print("Estimated pay:", round(estimated_pay, 2))

# Update stock after a sale
stock = 45
sold = 7
stock -= sold
print("Remaining stock:", stock)
