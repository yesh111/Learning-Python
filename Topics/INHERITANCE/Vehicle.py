class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand:", self.brand)

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def display(self):
        print(f"Bike Brand: {self.brand}, Type: {self.bike_type}")

class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

    def display(self):
        print(f"Car Brand: {self.brand}, Fuel Type: {self.fuel_type}")

b1 = Bike("Yamaha", "Sports")
c1 = Car("Toyota", "Petrol")


b1.display()
c1.display()
