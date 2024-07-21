# Write a Python program to convert degree to radian

import math

def degrees_to_radians(degrees):
    return math.radians(degrees)

degrees = 180
radians = degrees_to_radians(degrees)
print(f'{degrees} degrees is equal to {radians} radians')
