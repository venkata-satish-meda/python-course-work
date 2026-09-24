# Encapsulation practice: student marks

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)

    def average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.__marks)

    def result(self):
        return "Pass" if self.average() >= 40 else "Needs improvement"

student = Student("Anu")
for mark in [72, 81, 65, 78]:
    student.add_mark(mark)

print(student.name)
print("Average:", student.average())
print("Result:", student.result())
