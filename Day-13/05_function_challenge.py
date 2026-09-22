def second_largest(numbers):
    unique = sorted(set(numbers))
    return unique[-2]

numbers = [10, 5, 20, 8, 20, 15]
print(second_largest(numbers))
