class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

dog = Dog()
dog.speak()
dog.bark()
