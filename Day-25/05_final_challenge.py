# Simple ATM practice

balance = int(input("Enter balance: "))
pin = input("Enter PIN: ")
attempt = input("Enter PIN: ")
amount = int(input("Enter withdrawal: "))

if attempt != pin:
    print("Access denied")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print(balance)
