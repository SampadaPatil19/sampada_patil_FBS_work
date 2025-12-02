# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
"""
str = 'Gunjan Patil'

count = 0
words = 1

for ch in str:
    count += 1
    if ch == ' ':
        words += 1

print(words, count)
"""

def countCharAndWords(str):
    count = 0
    words = 1
    for ch in str:
        count += 1
        if ch == ' ':
            words += 1
    
    return f'Count of Words is {words} and count of char is {count}.'

str = input('Enter the String: ')
result = countCharAndWords(str)
print(result)