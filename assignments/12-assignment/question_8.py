# 8. Python Program to Remove the Characters of Odd Index Values in a String.

def removeOddCharacters(str):
    new_str = ''

    for ch in range(len(str)):
        if ch % 2 == 0 and str[ch] != " ":
            new_str += str[ch]

    return new_str

str = input('Enter the String: ')
result = removeOddCharacters(str)
print(result)