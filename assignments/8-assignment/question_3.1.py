# 3.1. Write a program to find sum of following series using functions : 
# 1!+ 2! + 3! + 4!+..... + n!

def sumOfSeries(n):
    fact = 1
    sum = 0
    if n == 0 or n == 1:
        return 1
    for i in range(1, n+1):
        fact *= i
        sum += fact
    return sum

n = int(input('Enter the count of terms in series: '))
result = sumOfSeries(n)
print(result)
