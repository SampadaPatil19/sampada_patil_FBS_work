# 8. Write a program find reverse of a number.

def reverseNumber(num):
    reverse = 0
    while num > 0:
        last_dig = num % 10
        reverse = reverse*10 + last_dig
        num = num // 10
    return reverse


num = int(input('Enter three-digit number: '))
result = reverseNumber(num)
print(result)