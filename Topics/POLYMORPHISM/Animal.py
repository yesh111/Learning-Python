class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


class Cow(Animal):
    def speak(self):
        print("Cow moos")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()
