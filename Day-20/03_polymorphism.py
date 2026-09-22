class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.sound())
