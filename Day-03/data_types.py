# Common Python data types

student_name = "Anil"          # str
age = 22                       # int
percentage = 78.5              # float
passed = True                  # bool
subjects = ["Python", "SQL"]   # list
marks = (78, 82, 75)           # tuple
skills = {"Python", "SQL"}     # set
student = {"name": "Anil", "age": 22}  # dict

values = [student_name, age, percentage, passed, subjects, marks, skills, student]
for value in values:
    print(value, "->", type(value).__name__)

# A practical dictionary record
employee = {
    "id": 101,
    "name": "Priya",
    "department": "IT",
    "salary": 32000.0,
    "active": True
}
print(employee["name"], employee["department"])
