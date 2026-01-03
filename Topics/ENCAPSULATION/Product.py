class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = None
        self.set_price(price)
        
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def display(self):
        print(f"Product: {self.name}, Price: {self.__price}")
        

p1 = Product("Laptop", 50000)
p1.display()

p1.set_price(55000)
p1.display()
