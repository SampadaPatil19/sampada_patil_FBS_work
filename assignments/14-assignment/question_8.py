"""
8. Write a Python program to find all the anagrams and group them 
together from a given list of strings."""

def group_anagrams(words):
    result = {}

    for word in words:
        sorted_word = "".join(sorted(word))

        if sorted_word not in result:
            result[sorted_word] = []

        result[sorted_word].append(word)

    return result


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = group_anagrams(words)

for value in groups.values():
    print(value)
