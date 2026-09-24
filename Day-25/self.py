# self refers to the current object

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print(self.holder, self.balance)

account = Account("Ravi", 10000)
account.deposit(2500)
account.show()
