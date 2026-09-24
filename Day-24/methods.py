# Methods describe object behaviour

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for name, price in self.items)

    def show(self):
        for name, price in self.items:
            print(name, price)

cart = ShoppingCart()
cart.add_item("Keyboard", 1200)
cart.add_item("Mouse", 650)
cart.show()
print("Total:", cart.total())
