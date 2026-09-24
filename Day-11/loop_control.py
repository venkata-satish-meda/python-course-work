# Loop control with while

attempts = 0
correct_pin = "2468"

while attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access granted")
        break
    print("Incorrect PIN")

if attempts == 3 and pin != correct_pin:
    print("Account temporarily locked")
