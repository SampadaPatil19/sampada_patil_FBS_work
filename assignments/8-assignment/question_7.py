# 7.  Write a program to find sum of digits of a number. 

def sumOfDigits(num):
    sum = 0
    while num > 0:
        last_dig = num % 10
        sum += last_dig
        num = num // 10
    return sum

num = int(input('enter a three-digit number: '))
result = sumOfDigits(num)
print(result)