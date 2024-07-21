#  Write a Python program to calculate surface volume and area of a 
# cylinder


import math

def cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

radius = 5
height = 10

volume = cylinder_volume(radius, height)
surface_area = cylinder_surface_area(radius, height)

print(f'The volume of the cylinder is {volume:.2f} cubic units')
print(f'The surface area of the cylinder is {surface_area:.2f} square units')
