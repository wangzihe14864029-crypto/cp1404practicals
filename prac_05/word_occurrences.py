"""
CP1404 Practical
Word Occurrences Counter
Estimate: 20 minutes
Actual: 24minutes
"""

def main():
    """Count how many times each word appears in a given string."""
    # a. Ask user for input text
    text = input("Text: ")

    # b. Split the text into words
    words = text.split()

    # c. Create dictionary to store word counts
    word_to_count = {}
    for word in words:
        word = word.lower()
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    # d. Sort the words alphabetically
    sorted_words = sorted(word_to_count.keys())

    # e. Find the length of the longest word for alignment
    max_length = max(len(word) for word in sorted_words)

    # f. Print each word and its count aligned
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")


main()
