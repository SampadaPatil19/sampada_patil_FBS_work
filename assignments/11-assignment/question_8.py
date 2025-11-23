# 8. Print 1 to 100 in snakes and ladder pattern.

"""
Short Logic Summary =>

Loop from row 0 to 9

For each row, calculate:
start = row*10 + 1
end = start + 9

If row is even → print forward
If row is odd → print backward
"""

def snake_and_ladder():
    for row in range(10):
        start = row*10 + 1
        end = start + 9

        if row % 2 == 0:
            for n in range(start, end+1):
                print(n, end = ' ')
        
        else:
            for n in range(end, start-1, -1):
                print(n, end = ' ')

        print()

snake_and_ladder()