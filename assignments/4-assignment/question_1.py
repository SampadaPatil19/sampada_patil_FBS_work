# 1. WAP to print all even numbers until n.

n = int(input('Enter the range: '))

for i in range(0, n+1):
    if i % 2 == 0:
        print(i)

