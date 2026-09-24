import random

# Small dice game
player = random.randint(1, 6)
computer = random.randint(1, 6)

print("Player:", player)
print("Computer:", computer)

if player > computer:
    print("Player score is higher")
elif player < computer:
    print("Computer score is higher")
else:
    print("Tie")

# Pick a support ticket from a queue
tickets = ["T101", "T102", "T103", "T104"]
print("Next ticket:", random.choice(tickets))
