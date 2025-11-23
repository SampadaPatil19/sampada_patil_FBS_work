#  9. WAP to print all numbers in a range divisible by a given number.

num = int(input('Enter the divisor: '))

start = int(input('Enter the starting of range: '))
end = int(input('Enter the ending of range: '))

for i in range(start, end+1):
    if i % num == 0:
        print(i)