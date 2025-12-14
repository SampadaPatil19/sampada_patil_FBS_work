# 2. Write a Python program to remove the intersection of a second set with a first set.

def remove_intersection(set1, set2):
    set1 = set1 - set2
    return set1


A = {1, 2, 3, 4, 5}
B = {3, 4, 6}

result = remove_intersection(A, B)
print("Set after removing intersection:", result)
