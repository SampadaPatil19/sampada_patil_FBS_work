# 1.  Write a program to find sum of all elements of list

def sumOfList(li):
    sum = 0
    for i in li:
        sum = sum + i

    return sum

li = [10, 20, 30, 40]
print(sumOfList(li))