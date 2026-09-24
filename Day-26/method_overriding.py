# A child class can provide its own implementation

class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()
