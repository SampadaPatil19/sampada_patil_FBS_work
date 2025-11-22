# 2.  Write a program to calculate the sum of following series where n is input by user.   
#     1/1! + 2/2! + 3/3! + 4/4! + ... N/N!


# 1st Approach
"""
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact

num = int(input('Enter the end of series: '))

sum_of_series = 0
for i in range(1, num+1):
    sum_of_series = sum_of_series + i/factorial(i)

print(f"Sum of the given series is {sum_of_series}") """



# 2nd Approach
def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num*factorial(num-1)

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
         sum += i/factorial(i)
    return sum
    
n = int(input('Enter the range os series: '))
result = sumOfSeries(n)
print(result)