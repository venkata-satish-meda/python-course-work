# List methods

tasks = ["email", "report", "meeting"]
tasks.append("backup")
tasks.extend(["testing", "deployment"])
print(tasks)

tasks.sort()
print("Sorted:", tasks)

completed = tasks.pop(0)
print("Completed:", completed)
print("Remaining:", tasks)

numbers = [10, 20, 10, 30, 10]
print("10 appears:", numbers.count(10), "times")
