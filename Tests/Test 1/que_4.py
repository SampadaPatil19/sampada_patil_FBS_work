# 4. . Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.  (Note: 1. Below diagram is of two joint rooms. 2. It is upper view of building.) 

interior_cost = float(input('Enter the cost of interior painting for walls per sq. ft.: '))
exterior_cost = float(input('Enter the cost of exterior painting for walls per sq. ft.: '))
area_of_one_wall = float(input('Enter the area of one wall of rooms: '))

total_interior_cost = 8 * area_of_one_wall * interior_cost

total_exterior_cost = 7 * area_of_one_wall * exterior_cost

total_cost = total_interior_cost +  total_exterior_cost

print(f"Cost of painting the interior of building's walls is {total_interior_cost}.")
print(f"Cost of painting the exterior of building's walls is {total_exterior_cost}.")
print(f"Cost of painting the all walls is {total_cost}.")