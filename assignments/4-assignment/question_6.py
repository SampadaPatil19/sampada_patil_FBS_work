# 6. WAP to check if a given number is prime number or not

num = int(input('Enter a positive number: '))

if num <= 1:
    is_prime = False

for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
is_prime = True

if is_prime:
    print(num, 'is prime number.')
else:
    print(num, 'is not prime number.')
