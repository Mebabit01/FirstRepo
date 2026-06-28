# Counting Pattern

word_counts = {}
line = input("Enter a line of text: ")

words = line.lower().split()

total_letters = len(line.replace(" ", ""))
print("Total number of letters is: ", total_letters)

total_words = len(words)

print("\nwords", words)

print("\nCounting....")

for word in words:
    word = word.strip(".,!?")
    word_counts[word] = word_counts.get(word, 0) + 1

print("\nCounts: ", word_counts)
print("Total number of words is: ", total_words)


