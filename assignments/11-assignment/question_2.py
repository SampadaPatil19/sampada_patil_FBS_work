# 2. Python Program to Merge Two Lists and Sort it


"""
Approach 1

def merge(li_1, li_2):
    merge = li_1 + li_2

    # bubble sort
    n = len(merge)

    for i in range(n):
        for j in range(0, n-i-1):
            if merge[j] > merge[j+1]:
                merge[j], merge[j+1] = merge[j+1], merge[j]
    return merge

li_1 = [10, 24, 13, 2]
li_2 = [1, 14, 21]

print(merge(li_1, li_2))
"""



"""
Approach 2
li_1 = [10, 20, 40]
li_2 = [50, 30, 60, 70]

merge = li_1 + li_2

sorted_list = sorted(merge)

print(f"List before sorting {merge}")
print(f"List after sorting {sorted_list}")
"""