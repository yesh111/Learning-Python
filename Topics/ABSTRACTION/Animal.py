class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   # calling parent constructor

    def sound(self):   # method overriding
        print(f"{self.name} says: Bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)   # calling parent constructor

    def sound(self):   # method overriding
        print(f"{self.name} says: Meow")

d = Dog("Tommy")
c = Cat("Kitty")

d.sound()
c.sound()
