# Task3: Word Counter

print("Welcome to the Word Counter!")

sentence = input("Please enter a sentence: ")

# Count the number of words in the sentence
words = sentence.split()  # split by whitespace
print("Number of words:", len(words))