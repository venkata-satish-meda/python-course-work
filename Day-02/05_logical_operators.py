# Day 2 - Logical operators
# and, or, and not work with True/False values.

age = 20
student = True

if age >= 18 and student:
    print("Adult student")

if age < 18 or student:
    print("At least one condition is True")

if not False:
    print("This is True")
