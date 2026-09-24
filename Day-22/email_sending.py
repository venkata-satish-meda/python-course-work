# SMTP sending practice.
# Use your own mail provider credentials before sending a real email.

import smtplib
from email.message import EmailMessage

sender = "your_email@example.com"
receiver = "customer@example.com"

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Test email"
message.set_content("This is a test message from a Python program.")

# Example structure only. Do not put passwords directly in source code.
# with smtplib.SMTP("smtp.example.com", 587) as server:
#     server.starttls()
#     server.login(sender, "APP_PASSWORD")
#     server.send_message(message)

print("Email message prepared.")
