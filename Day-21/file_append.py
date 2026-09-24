# Append new records without deleting old ones

with open("activity.log", "w", encoding="utf-8") as file:
    file.write("Application started\n")

with open("activity.log", "a", encoding="utf-8") as file:
    file.write("User logged in\n")
    file.write("Report generated\n")

with open("activity.log", "r", encoding="utf-8") as file:
    print(file.read())
