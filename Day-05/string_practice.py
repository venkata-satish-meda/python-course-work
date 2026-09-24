# String practice problems

# Mask a phone number
phone = "9876543210"
masked = "*" * 6 + phone[-4:]
print(masked)

# Count a character in a product code
code = "ABCA12A"
print("Number of A:", code.count("A"))

# Check whether a username is acceptable
username = input("Username: ").strip()
valid = len(username) >= 5 and " " not in username
print("Valid username:", valid)

# Remove extra spaces from a sentence
sentence = "Python   makes   automation   easier"
print(" ".join(sentence.split()))
