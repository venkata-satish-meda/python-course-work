text = input("Enter text: ")
vowels = "aeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count += 1

print("Vowels:", count)
