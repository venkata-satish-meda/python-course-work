class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

employee = Employee("Satish", 25000)
employee.display()
