# Find the first non-repeating character.

text = input("Enter text: ")

for ch in text:
    if text.count(ch) == 1:
        print(ch)
        break
else:
    print("No unique character")
