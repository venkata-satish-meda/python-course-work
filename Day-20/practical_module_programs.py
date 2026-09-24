import os
from datetime import datetime
import random

folder = "daily_reports"
os.makedirs(folder, exist_ok=True)

report_name = f"report_{datetime.now().strftime('%Y%m%d')}.txt"
report_path = os.path.join(folder, report_name)

ticket = random.randint(1000, 9999)
with open(report_path, "w", encoding="utf-8") as file:
    file.write(f"Support ticket: {ticket}\n")
    file.write(f"Created: {datetime.now()}\n")

print("Report created:", report_path)
