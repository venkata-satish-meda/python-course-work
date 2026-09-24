# Nested decisions

age = 24
has_license = True
has_vehicle = True

if age >= 18:
    if has_license:
        if has_vehicle:
            print("Ready to drive")
        else:
            print("License is valid, but no vehicle")
    else:
        print("License required")
else:
    print("Below legal driving age")

# Employee access
role = "manager"
active = True
if active:
    if role == "manager":
        print("Manager dashboard opened")
    else:
        print("Employee dashboard opened")
else:
    print("Account disabled")
