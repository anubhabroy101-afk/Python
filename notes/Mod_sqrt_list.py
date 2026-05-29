#WAP in Python to find the square root of a list of numbers.
import math
n = int(input("Enter the number of elements in the list: "))
a = []
for i in range(n):
    num = float(input(f"Enter a number {i+1}: "))
    a.append(num)

sqrt_a = []

for num in a:
    sqrt_a.append(math.sqrt(num))
print("The square root of the list is: ", sqrt_a)