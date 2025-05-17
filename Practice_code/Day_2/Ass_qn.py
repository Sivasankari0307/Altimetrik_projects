# write a function area of circle(radius) that returns the area of a circle.
import math

def area_of_circle(radius):
  return math.pi * radius**2

radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {area_of_circle(radius)}")