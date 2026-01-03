from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")

payments = [
    UPIPayment(),
    CardPayment()
]

for p in payments:
    p.pay(2000)
