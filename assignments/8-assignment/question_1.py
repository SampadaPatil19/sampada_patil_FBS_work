# 1. Write a program to calculate area of rectangle.

def areaOfRectangle(length, breadth):
    return length*breadth

length = int(input('Enter the length of Rectangle: '))
breadth = int(input('Enter the breadth of Rectangle: '))

result = areaOfRectangle(length, breadth)
print(f"Area of Rectangle is {result}.")