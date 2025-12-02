# 13. Python Program to count number of digits and letters in a string.
"""
Approach 1
str = 'gunjan 123'

total_digits = 0
total_letters = 0

for char in str:
    if char.isdigit():
        total_digits += 1
    # print(total_digits)
    elif char.isalpha():
        total_letters += 1
    
print(total_letters, total_digits)
"""

"""
Approach 2
str = 'gunjan 123'

total_digits = 0
total_letters = 0

for char in str:
    if ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
        total_letters += 1
    
    elif ('0' <= char <= '9'):
        total_digits += 1

print(total_digits, total_letters)
"""

def countDigitsAndLetters(str):
    digits = 0
    letters = 0

    for char in str:
        if ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            letters += 1
        
        elif ('0' <= char <= '9'):
            digits += 1

    return f"Letters in given string are {letters} and Digits in given string are {digits}."

str = input('What is your String? ')
output  = countDigitsAndLetters(str)
print(output)