# String handling in customer data

customer_name = "  Priya Sharma  "
clean_name = customer_name.strip()
print(clean_name)

email = "PRIYA.SHARMA@EXAMPLE.COM"
print(email.lower())

message = "Order ORD105 has been shipped"
print(message.replace("shipped", "delivered"))

# Build a simple username
first_name = "Ravi"
year = 2004
username = first_name.lower() + str(year)
print(username)
