# 9. Write a program to create three lists of numbers, their squares and cubes


def squares_and_cubes(list):
    square = []
    cubes = []

    for i in list:
        square.append(i**2)
        cubes.append(i**3)
    
    return square, cubes

list = [1, 2, 3, 4]

result = squares_and_cubes(list)

print(result)