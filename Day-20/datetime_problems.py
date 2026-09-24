from datetime import datetime, timedelta

start = datetime(2026, 9, 1, 10, 30)
end = start + timedelta(hours=3, minutes=45)

print("Start:", start)
print("End:", end)
print("Duration:", end - start)

# Subscription expiry
purchase = datetime(2026, 9, 23)
expiry = purchase + timedelta(days=30)
print("Expiry date:", expiry.date())
