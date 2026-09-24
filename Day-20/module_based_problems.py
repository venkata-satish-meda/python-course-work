import math
import random
from datetime import date

# Generate a simple invoice number
invoice_number = f"INV-{date.today().strftime('%Y%m%d')}-{random.randint(100,999)}"
print(invoice_number)

# Calculate a circular storage area
diameter = 20
radius = diameter / 2
print("Area:", round(math.pi * radius ** 2, 2))
