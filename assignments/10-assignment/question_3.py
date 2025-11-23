# 3. Write a program to find the second largest element in the list. 

def secondLargest(li):
    max_item = li[0]
    sec_max = 0
    for i in li:
        if i > max_item:
            sec_max = max_item
            max_item = i
        
        elif i > sec_max:
            sec_max = i
    
    return sec_max

li = [18, 23, 46, 84, 2, 10]
result = secondLargest(li)
print(f"Second largest element of list is {result}")