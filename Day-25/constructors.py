# Constructors initialize objects

class Vehicle:
    def __init__(self, number, model, price):
        self.number = number
        self.model = model
        self.price = price

    def display(self):
        print(self.number, self.model, self.price)

vehicle = Vehicle("TS09AB1234", "Swift", 850000)
vehicle.display()
