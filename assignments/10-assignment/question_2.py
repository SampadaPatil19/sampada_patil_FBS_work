# 2.  Write a program to find maximum and minimum element in a list.

def maxElement(li):
    max_item = li[0]

    for i in range(len(li)):
        if li[i] > max_item:
            max_item = li[i]

    return max_item

def minElement(li):
    min_item = li[0]

    for i in range(len(li)):
        if li[i] < min_item:
            min_item = li[i]
    
    return min_item

li = [10, 45, 102, 13, 23, 2, 90]
max_element = maxElement(li)
min_element = minElement(li)
print(f"Maximum element of the list is {max_element}.")
print(f"Minimum element of the list is {min_element}.")
