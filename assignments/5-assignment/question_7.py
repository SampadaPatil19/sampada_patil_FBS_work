# 7. Write a program to print first n prime numbers.

n = int(input('Enter the range: '))

for num in range(1, n+1):
    if num <= 1:
        is_prime = False
    
    else:
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num)