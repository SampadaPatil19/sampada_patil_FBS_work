# 4.  Write a program to print pattern  
# 10101  
# 01010  
# 10101  
# 01010  
# 10101  

def printPattern(rows):
    for i in range(rows):
        line = ''
        for j in range(rows):
            if (i+j) % 2 == 0:
                line += '1'
            else:
                line += '0'
        print(line)

rows = int(input('Enter the number of rows: '))
printPattern(rows)