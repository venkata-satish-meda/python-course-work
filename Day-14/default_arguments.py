# Default arguments

def delivery_charge(distance, charge_per_km=10):
    return distance * charge_per_km

print(delivery_charge(8))
print(delivery_charge(8, 15))

def greet_customer(name, message="Thank you for shopping with us."):
    print(f"Hello {name}. {message}")

greet_customer("Anu")
greet_customer("Ravi", "Your order has been shipped.")
