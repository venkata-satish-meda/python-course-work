# Dictionary methods

employee = {"name": "Meena", "department": "HR", "salary": 36000}

print(employee.keys())
print(employee.values())
print(employee.items())

employee.update({"salary": 39000, "city": "Hyderabad"})
print(employee)

removed = employee.pop("city")
print("Removed:", removed)
print(employee)

print("Phone:", employee.get("phone", "Not available"))
