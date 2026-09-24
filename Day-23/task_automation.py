# Automate a small repetitive task

tasks = [
    {"name": "backup files", "done": True},
    {"name": "send report", "done": False},
    {"name": "check emails", "done": False},
]

completed = 0

for task in tasks:
    if task["done"]:
        completed += 1
        continue

    print("Pending task:", task["name"])

print("Completed tasks:", completed)
print("Pending tasks:", len(tasks) - completed)
