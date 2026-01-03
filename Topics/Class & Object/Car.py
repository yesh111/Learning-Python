class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("------------------")
car1 = Car("Toyota", "Fortuner", 3500000)
car2 = Car("Hyundai", "Creta", 1800000)

car1.display_details()
car2.display_details()