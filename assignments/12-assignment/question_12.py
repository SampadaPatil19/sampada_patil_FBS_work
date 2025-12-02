# 12. Python Program to count number of lowercase characters in a string.

"""str = 'Gunjan'
count = 0

for ch in str:
    if ch.islower():
        count += 1
print(count)"""

def countLowerCase(str):
    count = 0

    for char in str:
        if char.islower():
            count += 1
    
    return count

str = input('enter the String: ')
result = countLowerCase(str)
print(result)