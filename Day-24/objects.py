# Creating and using objects

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print(f"{self.holder}: ₹{self.balance:.2f}")

account1 = BankAccount("Kiran", 25000)
account2 = BankAccount("Anu", 18000)

account1.show_balance()
account2.show_balance()
