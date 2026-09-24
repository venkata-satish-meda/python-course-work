# Data type practice

cart = ["Keyboard", "Mouse", "USB Cable"]
cart.append("Headset")
print("Cart:", cart)

unique_cities = {"Hyderabad", "Chennai", "Hyderabad", "Pune"}
print("Unique cities:", unique_cities)

order = ("ORD101", 1499.50, "Paid")
print("Order ID:", order[0])
print("Amount:", order[1])

customer = {"name": "Kiran", "orders": 4}
customer["orders"] += 1
print(customer)

# Find the average from integer values
marks = [65, 72, 81, 76]
print("Average:", sum(marks) / len(marks))
