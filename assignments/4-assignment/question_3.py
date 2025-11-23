# 3. WAP to print sum of series upto n.

n = int(input('Enter the end term of series: '))

sum = 0

for i in range(0, n+1):
    sum = sum + i

print(sum)