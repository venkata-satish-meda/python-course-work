# Python introduction practice

name = input("Enter your name: ").strip()
course = input("Enter your course: ").strip()
print(f"Hello {name}, welcome to the {course} course.")

# A small billing example
item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"{quantity} x {item} = ₹{total:.2f}")
