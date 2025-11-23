# 3. Program to find quotient and remainder of two numbers.
divisor = int(input('Enter the divisor: '))
dividend = int(input('Enter the dividend: '))

quotient = dividend // divisor
reminder = dividend % divisor

print(f'quotient is {quotient} and reminder is {reminder}')
