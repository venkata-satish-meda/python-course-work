with open("notes.txt", "r") as file:
    text = file.read()

print("Characters:", len(text))
print("Words:", len(text.split()))
