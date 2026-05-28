# WAP in python to a calculate the area and perimeter of a circle
import math

r=int(input("Enter the radius of the circle : "))
a=math.pi*pow(r,2)
p=2*math.pi*r
print("The area of the circle is : ",a)
print("The perimeter of the circle is : ",p)
