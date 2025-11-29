# 3.2. Write a program to find sum of following series using functions :
# 1^1 + 2^2 + 3^3+ ...... n^n

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    
    return sum

n = int(input('How many terms  are there in series: '))
result = sumOfSeries(n)
print(result)