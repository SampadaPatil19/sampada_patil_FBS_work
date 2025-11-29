# 3.0 Write a program to find sum of following series using functions :
# a.   1+ 2 + 3 + 4+..... + n 

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input('How many terms are there in series: '))
result = sumOfSeries(n)
print(result)