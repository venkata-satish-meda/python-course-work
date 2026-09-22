class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")
print(car.brand)
print(car.wheels)
