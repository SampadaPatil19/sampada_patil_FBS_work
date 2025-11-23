# 11. Find the area and circumference of circle.
# area of circle = 3.14 * radius**2
# circumference of  circle = 2 * 3.14 * radius

def areaOfCircle(radius):
    sq_of_radius = radius**2
    return 3.14 * sq_of_radius

def circumferenceOfCircle(radius):
    return 2 * 3.14 * radius

radius = int(input('Enter the radius of Circle: '))

area = areaOfCircle(radius)
circunference = circumferenceOfCircle(radius)

print(f'Area of Circle is {area}.\ncircumference of Circle is {circunference}.')