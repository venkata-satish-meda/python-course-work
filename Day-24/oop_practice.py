# OOP practice: employee payroll

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def monthly_pay(self):
        allowance = self.basic_salary * 0.10
        return self.basic_salary + allowance

    def display(self):
        print(self.name, "->", self.monthly_pay())

employees = [
    Employee("Ravi", 35000),
    Employee("Priya", 42000),
    Employee("Kiran", 39000)
]

for employee in employees:
    employee.display()
