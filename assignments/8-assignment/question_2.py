# 2. Write a program to calculate area of circle.

def areaOfCircle(radius):
    return 3.14*radius**2

radius = float(input('Enter the radius of Circle: '))
result = areaOfCircle(radius)
print(result)