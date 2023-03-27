# Write a class that meets these requirements.
#
# Name:       Circle
#
# Required state:
#    * radius, a non-negative value
#
# Behavior:
#    * calculate_perimeter()  # Returns the length of the perimater of the
# circle
#    * calculate_area()       # Returns the area of the circle
#
# Example:
#    circle = Circle(10)
#
#    print(circle.calculate_perimeter())  # Prints 62.83185307179586
#    print(circle.calculate_area())       # Prints 314.1592653589793
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

import math


class Circle:
    def __init__(circle, radius):
        if radius < 0:
            raise ValueError
        else:
            circle.radius = radius

    def calculate_perimeter(circle):
        perimeter = 2 * math.pi * circle.radius
        return perimeter

    def calculate_area(circle):
        area = math.pi * (circle.radius ** 2)
        return area


# Test Example:
circle = Circle(10)

print(circle.calculate_perimeter())  # Prints 62.83185307179586
print(circle.calculate_area())       # Prints 314.1592653589793

#     method calculate_perimeter(self)
#         returns 2 * math.pi * self.radius

#     method calculate_area(self)
#         returns math.pi * (self.radius squared)
