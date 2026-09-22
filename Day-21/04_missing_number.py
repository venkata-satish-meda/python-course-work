numbers = [1, 2, 3, 5, 6]
n = 6

expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing:", expected - actual)
