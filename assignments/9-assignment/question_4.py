"""
4. Write a program to find sum of n numbers using recursion
1+2+3+4+...+n
"""
def sumOfNumbers(terms):
    if (terms == 0):
        return 0
    else:
        return terms + sumOfNumbers(terms - 1)
        
terms = int(input('Enter the number of terms in series: '))
print(sumOfNumbers(terms))