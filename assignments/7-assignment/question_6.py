#  6. 
# python program to print hollow inverted half pyramid
# pattern using numbers

N = 5

for i in range(1, N+1):
    for j in range(i, N+1):
        if i == 1 or j == i or j == N:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
