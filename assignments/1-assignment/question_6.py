# 6. Write a Program to input two angles from user and find third angle of the triangle.

angle_1 = int(input('Enter the first angle: '))
angle_2 = int(input('Enter the second angle: '))

angle_3 = 180 - (angle_1+angle_2)

print(f'Third angle of triangle is {angle_3}')