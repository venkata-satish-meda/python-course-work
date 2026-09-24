# Dictionary practice with student records

student = {
    "id": 101,
    "name": "Ravi",
    "python": 82,
    "sql": 76,
    "attendance": 88
}

print(student["name"])
student["python"] = 86
student["status"] = "Active"

average = (student["python"] + student["sql"]) / 2
print("Average:", average)
print(student)

# Search a product price
products = {"keyboard": 1200, "mouse": 650, "monitor": 8500}
item = input("Product: ").lower()
print(products.get(item, "Product not found"))
