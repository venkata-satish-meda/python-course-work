number = int(input("Enter number: "))

if number < 2:
    print("Not prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
