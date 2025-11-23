# 7. Write a program to find sum of digits using recursion. 

def sumOfDigit(num):
    if (num <= 0):
        return 0
    else:
        last_digit = num % 10
        return last_digit + sumOfDigit(num // 10)
    
num = int(input('Enter the number: '))
print(sumOfDigit(num))