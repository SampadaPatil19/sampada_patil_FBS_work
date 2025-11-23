# 10. Write a program to calculate area of an equilateral triangle.
import math

def areaOfEquilateralTriangle(side):
    side_sq = side**2
    area = (math.sqrt(3)/4) * side_sq
    return area

side = int(input('Enter the side of equilateral triangle: '))
area = areaOfEquilateralTriangle(side)
print(f'Area of equilateral triangle is {area} sq. cm')