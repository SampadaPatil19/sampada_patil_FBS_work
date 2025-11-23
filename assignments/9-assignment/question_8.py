# 8. Write a program to check whether a number is prime or not using recursion.
def isPrime(num, i=2):
    # Numbers <= 1 are not prime
    if num <= 1:
        return "Not Prime"

    # If i*i > num, no divisor found → prime
    if i * i > num:
        return "Prime"

    # If divisible → not prime
    if num % i == 0:
        return "Not Prime"

    # Recursive call
    return isPrime(num, i + 1)


num = int(input("Enter the number: "))
print(isPrime(num))
