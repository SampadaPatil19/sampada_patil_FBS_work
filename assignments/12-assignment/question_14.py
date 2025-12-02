# 14. Python Program to count the occurrences of ach word in a string. 
"""
For given char: 

str = 'Sampada'
count = 0
new_str = []

for ch in str:
    new_str.append(ch)
    if ch == 'a' in new_str:
        count += 1
print(count)
"""

def countOfEachWord(string):
    words = string.split()
    words_count = {}

    for w in words:
        if w not in words_count:
            words_count[w] = 1
        
        else:
            words_count[w] += 1

    return f"Count of each words is {words_count}"

string = input('Enter a Statement: ')
output = countOfEachWord(string)
print(output)