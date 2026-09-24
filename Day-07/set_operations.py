# Set operations

python_students = {"Ravi", "Priya", "Kiran", "Anu"}
sql_students = {"Priya", "Kiran", "Vijay"}

print("Both courses:", python_students & sql_students)
print("Python only:", python_students - sql_students)
print("All students:", python_students | sql_students)
print("Only one course:", python_students ^ sql_students)

print("All SQL students included in all students:",
      sql_students <= (python_students | sql_students))
