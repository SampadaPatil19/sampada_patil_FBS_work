# 1. Write a program to check if the given number is positive or negative.

num = int(input('Enter the number: '))

if num == 0:
    print('Number is Neutral.')
elif num > 0:
    print('Number is Positive.')
else:
    print('Number is Negative.')