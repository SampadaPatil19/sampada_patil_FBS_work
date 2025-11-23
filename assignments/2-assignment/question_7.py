# 7. Find the sum of three-digit number.

num = int(input('Enter a three-digit number: '))

sum = 0

while num > 0:
    last_digit = num % 10
    sum += last_digit
    num = num // 10

print(sum)