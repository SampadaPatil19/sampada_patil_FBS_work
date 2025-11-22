# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

radius = 20
length = 50
breadth = 40

# question is about fencing, so find perimeter and circumference
perimeter_of_rect = 2 * length + breadth   # only one breadth bcoz other is covered as diameter of circle

cir_of_circle = 3.14*radius     # it's not 2*3.14*r bcoz using half circle

total_fencing = 5 * (perimeter_of_rect + cir_of_circle)

total_cost = 35 * total_fencing

print(f"{total_cost} is the total cost of fencing the field.")