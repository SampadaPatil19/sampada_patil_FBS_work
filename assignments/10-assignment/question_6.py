# 6.  Write a program to remove duplicates from the list.

def removeDuplicates(li):
    unique_list = []
    for i in li:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

li = [10, 40, 20, 20, 50]
result = removeDuplicates(li)
print(f"List after removing duplicates is {result}")


# 2nd Approach
