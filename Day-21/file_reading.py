# Reading a text file

file_name = "students.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"{file_name} does not exist yet.")

# Reading from a known string-like file format
with open("demo_read.txt", "w", encoding="utf-8") as file:
    file.write("Ravi,Python\nPriya,SQL\n")

with open("demo_read.txt", "r", encoding="utf-8") as file:
    print(file.read())
