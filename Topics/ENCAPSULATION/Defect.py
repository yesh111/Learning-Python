class Defect:
    def __init__(self, name, price):
        self.name = name
        self.price = price   # public variable


d = Defect("Laptop", 50000)

d.price = -20000   # ❌ invalid value allowed
print(d.price)
