# 1.  Write a program to print first n prime numbers.

 

def printPrimeInRange(start, end):
    for num in range(start, end+1):
        is_prime = True
        if num > 1:
            for i in (2, num):
                if num % i == 0:
                    is_prime = False
                    break
                print(num, end=' ')

start = int(input('Enter the start of range: '))
end = int(input('Enter the end of range: '))
result = printPrimeInRange(start, end)