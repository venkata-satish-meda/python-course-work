a = input("Enter first word: ").replace(" ", "").lower()
b = input("Enter second word: ").replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not anagram")
