# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x). 


def dict_series():
    n = int(input("Enter a number: "))

    result = {}

    for x in range(1, n + 1):
        result[x] = x * x

    print(result)

dict_series()
