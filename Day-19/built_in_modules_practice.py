import math
import random
from datetime import date

amounts = [1200, 850, 4300, 990]
print("Rounded average:", round(sum(amounts) / len(amounts), 2))
print("Largest amount:", max(amounts))
print("Random amount:", random.choice(amounts))
print("Today:", date.today())
print("Square root of 256:", math.sqrt(256))
