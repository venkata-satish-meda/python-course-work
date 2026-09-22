# Move all zeros to the end.

numbers = list(map(int, input("Enter numbers: ").split()))
result = [n for n in numbers if n != 0]
result += [0] * (len(numbers) - len(result))

print(result)
