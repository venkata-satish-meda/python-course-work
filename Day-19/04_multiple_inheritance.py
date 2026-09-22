class Father:
    def father_method(self):
        print("Father")

class Mother:
    def mother_method(self):
        print("Mother")

class Child(Father, Mother):
    pass

child = Child()
child.father_method()
child.mother_method()
