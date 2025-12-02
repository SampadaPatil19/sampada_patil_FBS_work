# alphabet pattern pyramid

n = 5
for i in range(1, n+1):
    # Print leading spaces
    spaces = n - i
    print(" " * spaces, end="")
    # Print letters
    for j in range(2 * i - 1):
        print(chr(ord('A') + j), end=" ")
    print()
