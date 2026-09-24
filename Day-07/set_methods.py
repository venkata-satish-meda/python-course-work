# Set methods in practical data cleaning

registered = {"A101", "A102", "A103", "A104"}
attended = {"A101", "A103"}

print("Present:", attended)
print("Absent:", registered - attended)

attended.add("A105")
attended.discard("A102")
print("Attendance:", attended)

# Safe removal
attended.discard("A999")
print(attended)
