class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount
            print(f"{self.name} deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive")
        elif amount > self.balance:
            print(f"{self.name}: Insufficient balance")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}. Balance: {self.balance}")


acc1 = BankAccount(101, "Bob", 5000)
acc2 = BankAccount(102, "Ram", 10000)
acc3 = BankAccount(103, "Ravi", 2000)

acc1.deposit(2000)
acc1.withdraw(1000)

acc2.withdraw(3000)
acc2.deposit(500)

acc3.withdraw(5000)   # insufficient balance
acc3.deposit(1500)


