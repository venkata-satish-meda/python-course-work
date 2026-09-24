# Prepare an email with an attachment

from email.message import EmailMessage
from pathlib import Path

message = EmailMessage()
message["From"] = "company@example.com"
message["To"] = "client@example.com"
message["Subject"] = "Invoice"
message.set_content("Please find the invoice attached.")

attachment = Path("invoice.txt")
attachment.write_text("Invoice ORD5001\nAmount: 2500", encoding="utf-8")

message.add_attachment(
    attachment.read_bytes(),
    maintype="text",
    subtype="plain",
    filename=attachment.name
)

print("Attachment added:", attachment.name)
