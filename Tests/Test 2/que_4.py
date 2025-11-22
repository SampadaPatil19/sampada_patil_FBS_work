# Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

area_of_wall = float(input('Enter the area of single wall in sq. unit: '))

cost_of_interior = float(input('Enter the cost for interior of single wall: '))

total_area_of_walls = 4 * area_of_wall

total_cost = total_area_of_walls * cost_of_interior

print(f"{total_cost} is the total cost for interior of four equal sized walls.")