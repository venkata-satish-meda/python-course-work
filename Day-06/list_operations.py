# List operations

sales_week1 = [12000, 14500, 9800]
sales_week2 = [15400, 16100, 13200]

all_sales = sales_week1 + sales_week2
print("All sales:", all_sales)

print("First three:", all_sales[:3])
print("Last two:", all_sales[-2:])

# Find sales above a target
target = 14000
for sale in all_sales:
    if sale > target:
        print("Above target:", sale)
