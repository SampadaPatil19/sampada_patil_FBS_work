"""
7.  Given two sets of numbers, write a Python program to find the missing 
numbers in the second set as compared to the first and vice versa. 
Use the Python set.
"""

def find_missing(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    return missing_in_set2, missing_in_set1


A = {1, 2, 3, 4, 5}
B = {3, 4, 6, 7}

m1, m2 = find_missing(A, B)

print("Missing in second set:", m1)
print("Missing in first set:", m2)
