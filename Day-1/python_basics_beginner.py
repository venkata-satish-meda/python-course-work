# Python Basics - Beginner Practice
# ==================================
# Start here if you are learning Python from zero.
# Run each section separately and change the examples to practice.

# --------------------------------------------------
# 1. PRINTING
# --------------------------------------------------

print("Hello, World!")
print("My name is Satish")
print(10)
print(10 + 20)


# --------------------------------------------------
# 2. COMMENTS
# --------------------------------------------------

# This is a single-line comment.
# Python ignores comments.

print("Comments help explain code.")


# --------------------------------------------------
# 3. VARIABLES
# --------------------------------------------------

name = "Satish"
age = 21
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print("Name:", name)
print("Age:", age)


# --------------------------------------------------
# 4. BASIC DATA TYPES
# --------------------------------------------------

name = "Satish"       # str
age = 21              # int
percentage = 59.1     # float
passed = True          # bool

print(type(name))
print(type(age))
print(type(percentage))
print(type(passed))


# --------------------------------------------------
# 5. STRINGS
# --------------------------------------------------

first_name = "Venkata"
last_name = "Satish"

print(first_name)
print(first_name + " " + last_name)
print(len(first_name))
print(first_name.upper())
print(first_name.lower())

message = f"My name is {first_name} {last_name}"
print(message)


# --------------------------------------------------
# 6. NUMBERS
# --------------------------------------------------

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Power


# --------------------------------------------------
# 7. USER INPUT
# --------------------------------------------------

name = input("Enter your name: ")
print("Hello", name)

# input() always gives a string.
age = int(input("Enter your age: "))
print("Your age is", age)


# --------------------------------------------------
# 8. TYPE CONVERSION
# --------------------------------------------------

number = "100"

integer_number = int(number)
decimal_number = float(number)
text_number = str(100)

print(integer_number)
print(decimal_number)
print(text_number)

print(type(integer_number))
print(type(decimal_number))
print(type(text_number))


# --------------------------------------------------
# 9. COMPARISON OPERATORS
# --------------------------------------------------

a = 10
b = 20

print(a == b)   # Equal
print(a != b)   # Not equal
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal
print(a <= b)   # Less than or equal


# --------------------------------------------------
# 10. LOGICAL OPERATORS
# --------------------------------------------------

age = 21
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# --------------------------------------------------
# 11. IF STATEMENT
# --------------------------------------------------

age = 20

if age >= 18:
    print("You are an adult.")


# --------------------------------------------------
# 12. IF - ELSE
# --------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")


# --------------------------------------------------
# 13. IF - ELIF - ELSE
# --------------------------------------------------

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# --------------------------------------------------
# 14. NESTED IF
# --------------------------------------------------

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")


# --------------------------------------------------
# 15. LIST
# --------------------------------------------------

fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(len(fruits))

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)


# --------------------------------------------------
# 16. LIST INDEXING AND SLICING
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# --------------------------------------------------
# 17. TUPLE
# --------------------------------------------------

colors = ("red", "green", "blue")

print(colors)
print(colors[0])
print(len(colors))


# --------------------------------------------------
# 18. SET
# --------------------------------------------------

numbers = {10, 20, 30, 20, 10}

print(numbers)  # Duplicate values are removed.

numbers.add(40)
print(numbers)

numbers.remove(20)
print(numbers)


# --------------------------------------------------
# 19. DICTIONARY
# --------------------------------------------------

student = {
    "name": "Satish",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])

student["city"] = "Hyderabad"
print(student)


# --------------------------------------------------
# 20. FOR LOOP
# --------------------------------------------------

for i in range(5):
    print(i)


# --------------------------------------------------
# 21. FOR LOOP WITH LIST
# --------------------------------------------------

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 22. WHILE LOOP
# --------------------------------------------------

count = 1

while count <= 5:
    print(count)
    count = count + 1


# --------------------------------------------------
# 23. BREAK
# --------------------------------------------------

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# --------------------------------------------------
# 24. CONTINUE
# --------------------------------------------------

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# --------------------------------------------------
# 25. FUNCTIONS
# --------------------------------------------------

def greet():
    print("Hello, welcome to Python!")

greet()


# --------------------------------------------------
# 26. FUNCTION WITH PARAMETERS
# --------------------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Satish")
greet_user("Rahul")


# --------------------------------------------------
# 27. FUNCTION WITH RETURN
# --------------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# --------------------------------------------------
# 28. SIMPLE CALCULATOR FUNCTION
# --------------------------------------------------

def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

calculator(20, 5)


# --------------------------------------------------
# 29. STRING METHODS
# --------------------------------------------------

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.replace("python", "Python"))
print(text.startswith("python"))
print(text.endswith("programming"))


# --------------------------------------------------
# 30. LIST LOOP
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

print("Total:", total)


# --------------------------------------------------
# 31. SIMPLE PRACTICE PROGRAMS
# --------------------------------------------------

# Program 1: Check positive, negative or zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Program 2: Check even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program 3: Find the biggest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is bigger")
elif b > a:
    print("Second number is bigger")
else:
    print("Both are equal")


# Program 4: Print numbers from 1 to 10

for i in range(1, 11):
    print(i)


# Program 5: Sum numbers from 1 to 10

total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total)


# --------------------------------------------------
# BEGINNER ORDER TO LEARN
# --------------------------------------------------
#
# 1. print()
# 2. comments
# 3. variables
# 4. data types
# 5. strings
# 6. numbers
# 7. input()
# 8. type conversion
# 9. operators
# 10. if / elif / else
# 11. lists
# 12. tuples
# 13. sets
# 14. dictionaries
# 15. for loop
# 16. while loop
# 17. break / continue
# 18. functions
# 19. practice programs
#
# IMPORTANT:
# Do not just read the code.
# Type each example yourself, run it, and change the values.
