import math

# Find the smallest number that is divisible by two values
a, b = 12, 18
lcm = abs(a * b) // math.gcd(a, b)
print("LCM:", lcm)

# Calculate compound amount
principal = 10000
rate = 8
years = 2
amount = principal * math.pow(1 + rate / 100, years)
print("Amount:", round(amount, 2))
