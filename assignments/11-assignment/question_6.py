# 6. Python Program to Find the Union of two Lists 


def unionOfLists(list1, list2):
    union = []

    for item in list1:
        if item not in union:
            union.append(item)
    
    for item in list2:
        if item not in union:
            union.append(item)
    
    return union

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 9]

print(unionOfLists(list1, list2))