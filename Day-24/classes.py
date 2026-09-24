# A class represents a type of object

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print(f"{self.name} is studying {self.course}")

student1 = Student("Ravi", "Python Full Stack")
student2 = Student("Priya", "Python Full Stack")

student1.display()
student2.display()
