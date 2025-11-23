# 2. Write a program to check if given number is Armstrong or not using recursive function. 
def armStrongNumber(num, power):
    if (num <= 0):
        return 0
    
    else:
        last_digit = num % 10
        return last_digit**power + armStrongNumber(num //10, power)

def checkIfNumberIsArmStrong(num):
    if num == armStrongNumber(num, power):
        return 'Number is Armstrong Number.'
    else:
        return 'Number is not Armstrong Number.'

num = int(input('Enter the Number: '))
power = int(input('Enter the total digits in Number: '))

print(checkIfNumberIsArmStrong(num))