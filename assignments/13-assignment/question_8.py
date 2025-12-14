# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary 


def wordsCount(string):
    words = string.split()

    words_count = {}

    for w in words:
        if w not in words_count:
            words_count[w] = 1

        else:
            words_count[w] += 1

    return words_count

string = 'Gunjan Patil, Gunjan is me.'
print(wordsCount(string))

