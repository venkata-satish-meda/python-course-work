# Slicing practical data

email = "satish.meda@gmail.com"
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print("Username:", username)
print("Domain:", domain)

date = "2026-09-23"
print("Year:", date[:4])
print("Month:", date[5:7])
print("Day:", date[8:])

# Reverse a tracking code
tracking = "HYD45821"
print("Reverse:", tracking[::-1])
