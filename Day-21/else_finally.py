# else runs when no exception occurs; finally always runs

file = None

try:
    file = open("sample.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("sample.txt was not found.")
else:
    print("File content:", content)
finally:
    if file:
        file.close()
    print("File operation finished.")
