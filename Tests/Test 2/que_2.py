# 2. Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”. Eg : - 428 , 214 etc

num = int(input('Enter the number: '))

unit_digit = num % 10

ten_digit = (num // 10) % 10

hundred_digit = num // 100

if (hundred_digit == 2*ten_digit and hundred_digit == 0.5*unit_digit):
    print('Yes, you have done it.')

else:
    print('Please try next time.')