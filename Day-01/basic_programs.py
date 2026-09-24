# Everyday beginner programs

# 1. Calculate a shopping bill
rice = 620
oil = 180
vegetables = 240
bill = rice + oil + vegetables
print("Shopping bill:", bill)

# 2. Calculate simple interest
principal = float(input("Principal amount: "))
rate = float(input("Interest rate: "))
years = float(input("Number of years: "))
interest = principal * rate * years / 100
print("Simple interest:", interest)
print("Final amount:", principal + interest)

# 3. Convert Celsius to Fahrenheit
celsius = float(input("Temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", round(fahrenheit, 2))

# 4. Calculate a monthly salary from daily wages
days = int(input("Days worked: "))
daily_wage = float(input("Daily wage: "))
print("Estimated salary:", days * daily_wage)
