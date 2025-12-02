# 10, Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
"""
str1 = 'gunjan'
str2 = 'Patil'

count1 = 0
count2 = 0

for ch in str1:
    count1 += 1

for ch in str2:
    count2 += 1

if count1 > count2:
    print(f'"{str1}" is larger.')
else:
    print(f'"{str2}" is larger.')
"""

def findLargerString(str1, str2):
    count1 = 0
    count2 = 0
    for ch in str1:
        count1 += 1
    
    for ch in str2:
        count2 += 1
    
    if count1 > count2:
        return f"'{str1}' is larger."
    else:
        return f"'{str2}' is larger."

str1 = input('What is the first String? ')
str2 = input('What is the second String? ')

result = findLargerString(str1, str2)
print(result)