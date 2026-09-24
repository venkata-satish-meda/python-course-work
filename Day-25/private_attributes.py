# Double underscore creates a private-style attribute

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

employee = Employee("Kiran", 40000)
employee.show_salary()
employee.increase_salary(3000)
employee.show_salary()
