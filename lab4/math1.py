import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input())

radians = degrees_to_radians(degrees)
print(radians)
