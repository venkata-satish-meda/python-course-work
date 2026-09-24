# Membership operators

allowed_roles = ["admin", "manager", "staff"]
role = input("Enter role: ").strip().lower()
print("Role accepted:", role in allowed_roles)

blocked_numbers = ["9999999999", "8888888888"]
phone = input("Enter phone number: ")
print("Number blocked:", phone in blocked_numbers)

skills = {"python", "sql", "html"}
print("Python skill present:", "python" in skills)
