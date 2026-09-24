# Decision making for an order

payment_status = "paid"
stock = 8
requested = 5

if payment_status == "paid":
    if requested <= stock:
        print("Order confirmed")
        stock -= requested
    else:
        print("Not enough stock")
else:
    print("Payment pending")

print("Remaining stock:", stock)

# Login decision
saved_user = "satish"
saved_password = "python123"
user = "satish"
password = "python123"

if user == saved_user and password == saved_password:
    print("Login successful")
else:
    print("Invalid username or password")
