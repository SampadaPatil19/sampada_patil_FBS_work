# 5. Python Program to Count the Number of Vowels in a String.

def findVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for item in str:
        if item in vowels:
            count += 1
    # print(count)
    return count


str = input('Enter a String: ')
result = findVowels(str)
print(result)