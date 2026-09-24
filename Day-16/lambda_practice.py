# Lambda practice with records

employees = [
    {"name": "Ravi", "salary": 42000},
    {"name": "Priya", "salary": 38000},
    {"name": "Kiran", "salary": 51000}
]

highest = max(employees, key=lambda employee: employee["salary"])
print("Highest salary:", highest)

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)
for employee in sorted_employees:
    print(employee["name"], employee["salary"])
