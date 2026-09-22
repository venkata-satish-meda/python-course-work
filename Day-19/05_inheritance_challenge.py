class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def work(self):
        print(self.name, "writes code")

developer = Developer("Satish")
developer.work()
