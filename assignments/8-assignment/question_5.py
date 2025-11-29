# 5. Sum of all prime numbers between 1 to n.

def sumOfPrime(n):
    sum = 0
    for num in range(n):
        if num <= 1:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                sum += num
    return sum
    
n = int(input('Enter the end of series: ' ))
result = sumOfPrime(n)
print(result)