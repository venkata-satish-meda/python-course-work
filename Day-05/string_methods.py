# Useful string methods

raw_status = "  payment successful  "
status = raw_status.strip().title()
print(status)

skills = "Python, SQL, HTML, CSS"
skill_list = [skill.strip() for skill in skills.split(",")]
print(skill_list)

message = "Your order number is ORD5001"
print("Contains order:", "order" in message.lower())
print("Message starts with Your:", message.startswith("Your"))

phone = "9876543210"
print("Only digits:", phone.isdigit())
