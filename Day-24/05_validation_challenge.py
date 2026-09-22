username = input("Username: ")
password = input("Password: ")

if len(username) >= 3 and len(password) >= 8:
    print("Valid")
else:
    print("Invalid")
