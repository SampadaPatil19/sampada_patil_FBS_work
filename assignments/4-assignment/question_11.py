# 11. WAP to check if given number Strong Number.

num = int(input('Enter a number to check if it is Strong Number or Not: '))

sum = 0

duplicate = num

while duplicate > 0:
    fact = 1

    last_digit = duplicate % 10

    for i in range(1, last_digit+1):
        fact *= i
    sum += fact
    
    duplicate = duplicate // 10

if sum == num:
    print('Strong Number')

else:
    print('Not a Strong Number')


print(sum)

