#  3.

# Python program print hollow half pyramid
# pattern using numbers

# pattern function

N = 5

for i in range(1, N+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == N:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

