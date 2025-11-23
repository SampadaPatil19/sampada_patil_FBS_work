#  4. Write a program to reverse the list.

li = [10, 20, 30, 40, 50]

# 1st Approach - slicing
print(li[::-1])    


# 2nd Approach - swapping
start_index = 0
end_index = len(li)-1

while start_index <= end_index:
    li[start_index], li[end_index] = li[end_index], li[start_index]

    start_index = start_index + 1

    end_index = end_index - 1

print(li)


# 3rd Approach - 

