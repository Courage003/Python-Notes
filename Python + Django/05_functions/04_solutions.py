import math

def circle_stata(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stata(3)

print("Area: ", a, "Circumference: ", c)

