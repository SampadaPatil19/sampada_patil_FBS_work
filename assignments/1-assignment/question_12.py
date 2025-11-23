# 12. Find the volume of sphere.
# volume of sphere = 4 / 3 * 3.14 * radius**3

def volOfSphere(radius):
    cube_of_radius = radius ** 3
    return 4/3 * 3.14 * cube_of_radius

radius = int(input('Enter the radius of sphere: '))

volume = volOfSphere(radius)

print(f'Volume of Sphere is {volume}. ')