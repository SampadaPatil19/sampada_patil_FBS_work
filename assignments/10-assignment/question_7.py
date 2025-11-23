# 7. Write a program to create a new list from existing list which contains cube of each number of list. 

def cubeList(li):
    unique_list = []
    for i in li:
         i = i ** 3
         unique_list.append(i)
    return unique_list

li = [1, 2, 3, 4]
result = cubeList(li)
print(result)