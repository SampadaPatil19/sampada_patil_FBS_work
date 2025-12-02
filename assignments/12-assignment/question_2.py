# 2. Python Program to Remove the nth Index Character from a Non-Empty String
"""
def removeFromIndex(s, n):
    lst = list(s)
    lst.pop(n)
    return ''.join(lst)

s = input('Enter a String: ')
n = int(input('Enter the index of character to be Removed: '))
result = removeFromIndex(s, n)
print("String after removing character at index", n, ":", result)

"""

# 2. Python Program to Remove the nth Index Character from a Non-Empty String
"""
def removeFromIndex(s, n):
    return s[:n] + s[n+1:]

s = input('Enter a String: ')
n = int(input('Enter the index of character to be Removed: '))
result = removeFromIndex(s, n)
print("String after removing character at index", n, ":", result)
"""