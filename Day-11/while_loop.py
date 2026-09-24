# While loop for repeated work

balance = 10000
withdrawals = [1200, 1800, 2500]
index = 0

while index < len(withdrawals):
    amount = withdrawals[index]
    if amount <= balance:
        balance -= amount
        print("Withdrawal:", amount, "Balance:", balance)
    else:
        print("Insufficient balance for:", amount)
    index += 1

# Countdown for a process
count = 5
while count > 0:
    print("Processing in", count)
    count -= 1
print("Done")
