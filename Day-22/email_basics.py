# Build an email message without sending it

from email.message import EmailMessage

message = EmailMessage()
message["From"] = "company@example.com"
message["To"] = "customer@example.com"
message["Subject"] = "Order confirmation"
message.set_content(
    "Hello, your order ORD105 has been confirmed.\n"
    "Thank you for shopping with us."
)

print(message)
