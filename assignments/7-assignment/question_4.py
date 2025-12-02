"""
    1
   232
  34543
 4567654
567898765
"""

# Code to print the number pattern
n = 5
for i in range(1, n+1):
    # Print leading spaces
    for j in range(n - i):
        print(' ', end='')
    # Print the increasing part
    for j in range(i, 2*i):
        print(j, end='')
    # Print the decreasing part
    for j in range(2*i-2, i-1, -1):
        print(j, end='')
    print()
