# 7.  Python Program to Calculate the Length of a String Without Using a Library Function

def lengthOfString(str):
    count = 0

    for ch in str:
        if ch != " ":
            count += 1
    
    return count

str = input('Enter the String: ')
result = lengthOfString(str)
print(result)