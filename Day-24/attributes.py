# Object attributes hold data

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show(self):
        print(self.name, self.price, self.stock)

product = Product("Keyboard", 1200, 15)
product.show()

product.stock -= 2
product.show()
