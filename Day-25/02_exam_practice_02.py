# Count words that appear more than once.

words = input("Enter words: ").lower().split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

for word, frequency in count.items():
    if frequency > 1:
        print(word, frequency)
