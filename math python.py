import math
def degree_to_radian(degree):
    return math.radians(degree)
def area_tra(height, base1, base2):
    return ((base1 + base2) / 2) * height
def area_poly(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
def area_parall(base, height):
    return base * height
