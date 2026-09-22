class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = Account(5000)
print(account.get_balance())
