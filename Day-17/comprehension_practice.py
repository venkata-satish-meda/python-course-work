# Comprehension practice

orders = [
    {"id": "ORD1", "amount": 1200},
    {"id": "ORD2", "amount": 700},
    {"id": "ORD3", "amount": 2300}
]

priority_orders = [
    order["id"] for order in orders if order["amount"] >= 1000
]
print(priority_orders)

order_values = {
    order["id"]: order["amount"]
    for order in orders
}
print(order_values)

unique_amounts = {order["amount"] for order in orders}
print(unique_amounts)
