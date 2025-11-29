# 9. Write a program to check if entered number is a palindrome or not.

def palindromeNumber(num):
    reverse = 0
    duplicate = num

    while duplicate > 0:
        last_dig = duplicate % 10
        reverse = reverse * 10 + last_dig
        duplicate = duplicate // 10

    return reverse

def checkPalindrome(num):
    if palindromeNumber(num) == num:
        print('Number is Palindrome.')
    else:
        print('Number is not Palindrome.')

num = int(input('Enter a number: '))
checkPalindrome(num)
