# Nested loops for a small timetable

for hour in range(1, 4):
    for minute in range(0, 60, 30):
        print(f"{hour:02d}:{minute:02d}")

# Compare products from two stores
store_a = ["Keyboard", "Mouse", "Monitor"]
store_b = ["Mouse", "Monitor", "Webcam"]

for item_a in store_a:
    for item_b in store_b:
        if item_a == item_b:
            print("Available in both stores:", item_a)
