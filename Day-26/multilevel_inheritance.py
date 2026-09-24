# Multilevel inheritance

class Person:
    def introduce(self):
        print("I am a person")

class Employee(Person):
    def work(self):
        print("I work for a company")

class Manager(Employee):
    def approve_leave(self):
        print("Leave approved")

manager = Manager()
manager.introduce()
manager.work()
manager.approve_leave()
