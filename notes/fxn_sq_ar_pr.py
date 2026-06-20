#WAP in python to find area and perimeter of a square 
def ar(a):
    return a**2
def pr(a):
    return a*4

x = int(input("Enter the side of the square: "))

ar = ar(x)
pr = pr(x)

print("The area of the square is",ar,"sq.units \nThe perimeter of the square is",pr,"units")
