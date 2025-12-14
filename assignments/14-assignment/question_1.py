#  Write a Python program to find elements in a given set that are not in another set.

def find_difference(set1, set2):
    result = set1 - set2
    return result


A = {1, 2, 3, 4, 5}
B = {3, 4, 6}

output = find_difference(A, B)
print("Elements in A but not in B:", output)


"""
def find_difference(set1, set2):
    return set1.difference(set2)
"""