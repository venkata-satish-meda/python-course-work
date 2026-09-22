class Grandparent:
    def show(self):
        print("Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

Child().show()
