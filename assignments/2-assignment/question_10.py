# 10. Write a program to reverse three-digit number.

num = int(input('Enter three-digit number: '))

reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse*10 + last_digit
    num = num // 10

print(f'Reverse of given three-digit number is {reverse}.')