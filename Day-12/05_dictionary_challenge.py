text = input("Enter text: ")
words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
