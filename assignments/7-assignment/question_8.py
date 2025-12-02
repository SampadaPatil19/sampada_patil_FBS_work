"""
1               1
1 2           2 1
1 2 3       3 2 1
1 2 3 4   4 3 2 1
1 2 3 4 5 4 3 2 1
"""

n = 5  # number of rows

for i in range(1, n + 1):
    
    # Left side increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    spaces = (n - i) * 4   # each "gap" = 4 spaces visually
    print(" " * spaces, end="")
    
    # Right side decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()
