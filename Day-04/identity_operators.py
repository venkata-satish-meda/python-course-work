# Identity operators compare object identity, not just values

first = [10, 20, 30]
second = first
third = [10, 20, 30]

print("first is second:", first is second)
print("first is third:", first is third)
print("first == third:", first == third)

# None is normally checked with is
result = None
if result is None:
    print("No result returned yet.")
