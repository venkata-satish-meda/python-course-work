text = input("Enter text: ").lower().replace(" ", "")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
