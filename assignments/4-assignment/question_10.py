# 10. WAP to check if given number is Perfect Number.

num = int(input('Enter a number to check if it is a perfect number: '))

sum_divisor = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisor = sum_divisor + i
    
print(sum_divisor)

if sum_divisor == num:
    print(f'{num} is a Perfect Number.')

else:
    print(f'{num} is not a Perfect Number.')
