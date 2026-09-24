# Local variables exist inside their function

def calculate_total():
    price = 1200
    quantity = 3
    total = price * quantity
    print("Inside function:", total)

calculate_total()

# price is intentionally not used outside the function.
