#WAP in Python to find the roots of a quadratic equation ax^2 + bx + c = 0
import math

# Taking coefficients as input
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = (b ** 2) - (4 * a * c)

print("Discriminant =", d)

# Check nature of roots
if d > 0: #Eg: x²+5x+6=0
    # Two different real roots
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    print("Two distinct real roots")
    print("Roots are:", root1, root2)

elif d == 0:#Eg: x²+4x+4=0
    # Equal roots
    root = -b / (2 * a)

    print("Two equal roots")
    print("Root =", root)

else:#Eg: x²+2x+5=0
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-d) / (2 * a)

    print("Complex roots")
    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")