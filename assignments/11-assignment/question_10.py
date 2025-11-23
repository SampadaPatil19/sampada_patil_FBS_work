# 10. Write a program to print list after removing even numbers.

def removeEvenNum(li):
    final_list = []

    for i in li:
        if i % 2 != 0:
            final_list.append(i) 
            # never do this => li.remove(i) [list shifts after every loop]
    
    return final_list

li = [1, 2, 3, 4, 5, 6, 7, 8]

print(removeEvenNum(li))