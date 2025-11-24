"""
Write a program to check if given number is Armstrong number or not.  
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
4*4*4*4)
"""

num = int(input('Enter the number: '))
number_of_digits = int(input('Enter the number of digits in given number: '))

duplicate = num
sum = 0

while num > 0:
    last_digit = num % 10
    sum = sum + last_digit**number_of_digits
    num = num // 10

if sum == duplicate:
    print('The given number is Armstrong.')
else:
    print('The given number is not Armstrong.')
