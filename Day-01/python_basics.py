# Basic syntax and simple calculations

student_name = "Satish"
age = 21
city = "Yanam"

print("Student:", student_name)
print("Age:", age)
print("City:", city)

# Calculate the total marks of three subjects
python = 78
sql = 72
html = 81
total = python + sql + html
average = total / 3

print("Total marks:", total)
print("Average:", round(average, 2))

# Convert minutes into hours and minutes
minutes = 185
hours = minutes // 60
remaining = minutes % 60
print(f"{hours} hour(s) {remaining} minute(s)")
