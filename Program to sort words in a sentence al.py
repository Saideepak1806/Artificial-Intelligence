sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("\nSorted sentence:")
for word in words:
    print(word)