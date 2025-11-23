# 3. Write a program to reverse a given number using recursive function.
def reverseNumber(num, reverse=0):
    if (num == 0):
        return reverse
    else:
        last_digit = num % 10
        reverse = (reverse*10) + last_digit
        return reverseNumber(num // 10, reverse)

num = int(input('Enter the Number: '))
print(reverseNumber(num))