print("1. Add")
print("2. Subtract")

choice = input("Choose: ")
a = int(input("First: "))
b = int(input("Second: "))

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
else:
    print("Invalid choice")
