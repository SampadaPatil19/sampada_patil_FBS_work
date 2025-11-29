# 4.  Sum of all odd numbers between 1 to n 
# 1, 2, 3, 4 ,5 

def sumOfOddNumbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum += i
    
    return sum

n = int(input('Enter the number of terms: '))
result = sumOfOddNumbers(n)
print(result)