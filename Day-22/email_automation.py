# Simple email automation flow

from email.message import EmailMessage

customers = [
    ("Ravi", "ravi@example.com"),
    ("Priya", "priya@example.com"),
]

for name, email in customers:
    message = EmailMessage()
    message["From"] = "support@example.com"
    message["To"] = email
    message["Subject"] = "Account update"
    message.set_content(
        f"Hello {name},\n\nYour account information is ready for review."
    )

    print("Prepared email for:", name)
    print("Recipient:", message["To"])
