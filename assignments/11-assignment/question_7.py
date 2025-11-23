# 7. Python Program to Find the Intersection of Two Lists

def intersectioOfLists(list1, list2):
    intersection = []

    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    
    return intersection

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 6, 5, 9, 8]

print(intersectioOfLists(list1, list2))