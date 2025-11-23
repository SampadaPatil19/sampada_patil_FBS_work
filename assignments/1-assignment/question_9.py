# 9. Write a program to enter base and height of a triangle and find its area.
# area of triangle = 1/2 x base x height

def areaOfTriangle(base, height):
    area_of_triangle = 0.5*base*height
    return area_of_triangle

base = int(input('Enter the base of triangle: '))
height = int(input('Enter the height of triangle: '))

area = areaOfTriangle(base, height)

print(f'Area of triangle is {area} sq.cm')