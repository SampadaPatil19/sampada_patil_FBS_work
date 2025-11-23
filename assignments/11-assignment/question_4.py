# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def secondLargeUsingBubbleSort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list[-2]

list = [10, 24, 12, 34, 30, 45]

result = secondLargeUsingBubbleSort(list)

print(f'Second Largest Element of List is {result}.')