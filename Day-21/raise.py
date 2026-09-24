# raise lets us reject invalid business data

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    balance = withdraw(10000, 2500)
    print("Remaining balance:", balance)
except ValueError as error:
    print("Transaction failed:", error)
