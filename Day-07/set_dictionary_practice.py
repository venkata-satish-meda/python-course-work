# Combined sets and dictionaries

employees = {
    101: {"name": "Ravi", "skills": {"Python", "SQL"}},
    102: {"name": "Priya", "skills": {"Python", "Django"}},
    103: {"name": "Kiran", "skills": {"Java", "SQL"}}
}

required = {"Python", "SQL"}

for employee_id, details in employees.items():
    if required <= details["skills"]:
        print(details["name"], "matches the required skills")

# Count product categories
items = ["phone", "laptop", "phone", "tablet", "laptop", "phone"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print(counts)
