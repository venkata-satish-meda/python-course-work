# Single inheritance example

class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def open_boot(self):
        print("Car boot opened")

car = Car()
car.start()
car.open_boot()
car.stop()
