# Arithmetic operators in business calculations

subtotal = 1850
tax = subtotal * 0.18
delivery = 60
total = subtotal + tax + delivery

print("Subtotal:", subtotal)
print("Tax:", round(tax, 2))
print("Delivery:", delivery)
print("Final total:", round(total, 2))

# Split a restaurant bill
bill = 1260
people = 4
print("Each person pays:", bill / people)

# Convert seconds to minutes and seconds
seconds = 367
print("Minutes:", seconds // 60)
print("Seconds:", seconds % 60)
