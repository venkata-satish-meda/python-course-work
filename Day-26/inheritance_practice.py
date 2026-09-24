# Inheritance practice: employee roles

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary

class Developer(Employee):
    def calculate_pay(self):
        return self.salary + 5000

class Intern(Employee):
    def calculate_pay(self):
        return self.salary + 1000

employees = [
    Developer("Ravi", 40000),
    Intern("Anu", 18000),
    Employee("Kiran", 30000)
]

for employee in employees:
    print(employee.name, "->", employee.calculate_pay())
