# Logical operators combine business rules

age = 23
has_license = True
can_drive = age >= 18 and has_license
print("Can drive:", can_drive)

marks = 72
attendance = 84
eligible_for_exam = marks >= 40 and attendance >= 75
print("Exam eligible:", eligible_for_exam)

role = "manager"
active = True
can_approve = role == "manager" and active
print("Can approve request:", can_approve)

amount = 1200
member = False
discount = amount >= 2000 or member
print("Discount available:", discount)
