from datetime import datetime, date, timedelta

now = datetime.now()
print("Current date and time:", now)
print("Date:", now.date())

joining_date = date(2026, 8, 15)
review_date = joining_date + timedelta(days=90)
print("Joining date:", joining_date)
print("Review date:", review_date)

birth_year = 2005
print("Approximate age:", date.today().year - birth_year)
