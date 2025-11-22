# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:  

length = float(input('Enter the length of given figure: '))
breadth = float(input('Enter the breadth of given figure: '))
radius = float(input('Enter the radius of given figure: '))


# Area of given figure
area_of_rectangle = length * breadth

area_of_circle = 3.14*radius**2

half_area_of_circle = 0.5 * area_of_circle

area_of_given_figure = area_of_rectangle + half_area_of_circle

print(f'Area of given figure is {area_of_given_figure}.')


# Perimeter of given figure
perimeter_of_circle = 2*3.14*radius

half_perimeter_of_circle = 0.5*perimeter_of_circle

perimeter_of_rectangle = 2*length + breadth

perimeter_of_given_figure = perimeter_of_rectangle + half_perimeter_of_circle

print(f'Perimeter of given figure is {perimeter_of_given_figure}.')
