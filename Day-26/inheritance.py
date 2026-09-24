# Basic inheritance

class Employee:
    def __init__(self, name):
        self.name = name

    def show_role(self):
        print(self.name, "is an employee")

class Developer(Employee):
    def write_code(self):
        print(self.name, "is writing Python code")

developer = Developer("Ravi")
developer.show_role()
developer.write_code()
