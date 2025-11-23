# 6. Write a program to print Fibonacci series using recursion.
def fibonacci(terms):
    if terms <= 1:
        return terms
    else:
        return fibonacci(terms - 1) + fibonacci(terms - 2)
    
terms = int(input('Enter the number of terms: '))
print(fibonacci(terms))

for i in range(terms):
    print(fibonacci(i), end=' ')