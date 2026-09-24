# Getters and setters control access to data

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = 0
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

product = Product("Monitor", 8500)
print(product.price)

product.price = 9000
print(product.price)
