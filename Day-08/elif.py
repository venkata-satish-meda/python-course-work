# Multiple conditions

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

temperature = 34
if temperature >= 40:
    print("Very hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Comfortable")
else:
    print("Cool")
