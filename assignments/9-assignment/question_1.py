"""
1. Write a program to find sum of following series using recursive functions:  
i. 1! + 2!  + 3! + 4! +..... + n!  
          Note : For fact and sum two recursive functions
"""

def factorial(num):
    if (num<0) :
        return 'negative number'
    elif (num == 0 or num == 1):
        return 1
    else:
        return num*factorial(num-1)

def sumOfSeries(num):
    if (num <= 0):
        return 0
    else:
        fact = 0
        for i in range(1, num+1):
            fact += factorial(i)
        return fact
    
num = int(input('Enter the number: '))
print(sumOfSeries(num))