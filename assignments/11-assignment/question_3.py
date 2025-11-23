# 3. Python Program to Sort the List According to the Second Element in Sublist.

def sortListBasedOnSecEle(li_1):
    n = len(li_1)

    for i in range(n):
        for j in range(0, n-i-1):
            if li_1[j][1] > li_1[j+1][1]:
                li_1[j][1], li_1[j+1][1] = li_1[j+1][1], li_1[j][1]
    
    return li_1

li = [[1, 3], [2, 1], [4, 2], [3, 5]]

print(sortListBasedOnSecEle(li))