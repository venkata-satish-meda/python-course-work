# Write a simple daily report

report = [
    "Daily Sales Report",
    "------------------",
    "Orders: 18",
    "Revenue: 24500",
    "Returns: 2"
]

with open("daily_report.txt", "w", encoding="utf-8") as file:
    for line in report:
        file.write(line + "\n")

print("Report saved.")
