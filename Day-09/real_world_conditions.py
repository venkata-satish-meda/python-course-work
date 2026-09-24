# Real-world condition practice

delivery_distance = 7
order_value = 1300

if order_value >= 1000:
    delivery_fee = 0
elif delivery_distance <= 5:
    delivery_fee = 40
else:
    delivery_fee = 70

print("Delivery fee:", delivery_fee)

# Overtime calculation
hours = 48
hourly_rate = 220

if hours > 40:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours - 40) * hourly_rate * 1.5
else:
    regular_pay = hours * hourly_rate
    overtime_pay = 0

print("Total pay:", regular_pay + overtime_pay)
