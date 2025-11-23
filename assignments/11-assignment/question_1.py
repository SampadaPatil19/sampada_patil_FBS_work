# 1. Python Program to Put Even and Odd elements of a List into two Different Lists 

def evenAndOddLists(li):
    even = []
    odd = []

    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd
    
list = [15, 20, 30, 40, 55, 60, 70]

even_list, odd_list = evenAndOddLists(list)

print(f"Even List is {even_list}")
print(f"Odd List is {even_list}")