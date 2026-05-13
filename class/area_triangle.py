#WAP in python to find the area of a triangle using Heron's formula
import math
# Taking sides of the triangle as input
a = int(input("Enter length of side a: "))
b = int(input("Enter length of side b: "))
c = int(input("Enter length of side c: "))
# Calculate semi-perimeter
s = (a + b + c) / 2
# Calculate area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of the triangle is:", area)