"""
3. Write a Python program to find all the unique words and count the 
frequency of occurrence from a given list of strings. Use Python set 
data type. 
"""

def count_word_frequency(string_list):
    words = []

    # Step 1: Split each string into words
    for sentence in string_list:
        words.extend(sentence.split())

    # Step 2: Create a set of unique words
    unique_words = set(words)

    # Step 3: Count frequency of each unique word
    frequency = {}
    for word in unique_words:
        frequency[word] = words.count(word)

    return frequency


strings = [
    "python is easy",
    "python is powerful",
    "easy learning python"
]

result = count_word_frequency(strings)

for word, count in result.items():
    print(word, ":", count)
