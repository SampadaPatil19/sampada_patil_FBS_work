"""
        A 
      A B C
    A B C D E 
  A B C D E F G
A B C D E F G H I
"""

rows = 5  # number of lines

for i in range(rows):
    # print spaces
    print("  " * (rows - i - 1), end="")
    
    # print characters
    ch = 65  # ASCII for 'A'
    for j in range(2*i + 1):   # number of letters in each row
        print(chr(ch), end=" ")
        ch += 1

    print()  # move to next line
