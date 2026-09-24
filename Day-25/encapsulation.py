# Encapsulation keeps related data and operations together

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account = BankAccount("Priya", 20000)
account.deposit(3000)
account.withdraw(4500)
print("Balance:", account.get_balance())
