# Recursion practice

def countdown(number):
    if number == 0:
        print("Start!")
        return
    print(number)
    countdown(number - 1)

countdown(5)

def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print(reverse_text("python"))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(8)])
