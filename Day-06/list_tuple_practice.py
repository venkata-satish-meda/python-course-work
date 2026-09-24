# Combined list and tuple practice

orders = [
    ("ORD101", 1200),
    ("ORD102", 850),
    ("ORD103", 2100),
    ("ORD104", 450)
]

total = 0
for order_id, amount in orders:
    total += amount
    if amount >= 1000:
        print(order_id, "qualifies for priority shipping")

print("Total order value:", total)

# Convert tuple to list when changes are required
address = ("Hyderabad", "Telangana")
address_list = list(address)
address_list.append("India")
print(address_list)
