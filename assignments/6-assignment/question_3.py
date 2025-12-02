# Alphabet pattern
"""
A
A B
A B C
A B C D
A B C D E
"""

# Code to print the alphabet pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(ord('A') + j - 1), end=' ')
    print()
