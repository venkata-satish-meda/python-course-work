a = set(map(int, input("Enter numbers: ").split()))
b = set(map(int, input("Enter numbers: ").split()))

print(sorted(a & b))
