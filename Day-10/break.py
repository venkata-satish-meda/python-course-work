# Stop processing when a condition is reached

transactions = [1200, 850, 4300, -1, 900]

for amount in transactions:
    if amount == -1:
        print("Invalid marker found. Stopping.")
        break
    print("Processed transaction:", amount)

# Search for the first unavailable product
products = ["keyboard", "mouse", "monitor", "webcam"]
requested = "monitor"

for product in products:
    if product == requested:
        print("Product found")
        break
