# 12. Write a program to check if given 3 digit number is a palindrome or not.

def checkPalindrome(num):
    duplicate = num
    reverse = 0

    while duplicate > 0:
        last_digit = duplicate % 10
        reverse = reverse*10 + last_digit
        duplicate = duplicate // 10
    
    return reverse

num = int(input('Enter the three-digit number: '))

if checkPalindrome(num) == num:
    print(f'{num} is a Palindrome.')
else:
    print(f'{num} is not a Palindrome.')
