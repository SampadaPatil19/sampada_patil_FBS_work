# pyramid * pattern for 5 rows

# Code to print the pyramid * pattern
for i in range(1, 6):
    # Print leading spaces
    for j in range(5 - i):
        print(' ', end='')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end='')
    print()
