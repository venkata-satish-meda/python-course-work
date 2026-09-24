# Import selected functions

from datetime import date, timedelta

today = date.today()
print("Today:", today)
print("After 30 days:", today + timedelta(days=30))

from math import factorial
print("6 factorial:", factorial(6))
