# 5. Write a program to find factorial using recursion.

def factorial(terms):
    if (terms < 0):
        return 0
    elif (terms == 0 or terms == 1):
        return 1
    else:
        return terms * factorial(terms - 1)
    
terms = int(input('Enter the terms: '))
print(factorial(terms))