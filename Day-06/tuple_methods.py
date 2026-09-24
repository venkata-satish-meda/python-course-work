# Tuple methods

months = ("Jan", "Feb", "Mar", "Apr", "Feb")
print("February count:", months.count("Feb"))
print("March position:", months.index("Mar"))

# A tuple can contain mutable data
order = ("ORD101", ["Keyboard", "Mouse"])
order[1].append("USB Cable")
print(order)
