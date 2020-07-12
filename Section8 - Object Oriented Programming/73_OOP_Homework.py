import math


class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)
# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distrance of the line


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
print()


# Problem 2
# Fill in the class
class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.height + self.radius)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
print()
