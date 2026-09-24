# Tuples are useful for fixed records

employee = (101, "Ravi", "Developer", 42000)
print("Employee ID:", employee[0])
print("Role:", employee[2])

coordinates = (17.3850, 78.4867)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Unpacking a fixed record
product = ("Keyboard", 1299, 12)
name, price, stock = product
print(name, price, stock)
