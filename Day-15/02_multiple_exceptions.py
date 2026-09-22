try:
    a = int(input())
    b = int(input())
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division")
