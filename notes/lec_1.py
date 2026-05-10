# WAP in Python to calculate simple interest
def block1():
    p = int(input("Enter the principal : "))
    t = int(input("Enter the time period : "))
    r = int(input("Enter the rate of interest : "))
    i = (p * t * r) / 100
    print("The simple interest is : ", i)

# WAP in Pyhton to calculate the area and perimeter of a sqare
def block2():
    l=int(input("Enter the side of the square : "))
    a=l*l
    print("The area of the square is : ",a)
    p=4*l
    print("The perimeter of the square is : ",p)

# WAP in python to a calculate the area and perimeter of a circle
def block3():
    import math
    r=int(input("Enter the radius of the circle : "))
    a=math.pi*pow(r,2)
    p=2*math.pi*r
    print("The area of the circle is : ",a)
    print("The perimeter of the circle is : ",p)

# WAP to check a leap year
def block4():
    y=int(input("Enter the year : "))
    if (y%4==0 and y%100!=0) or (y%400==0): #Keep in mind that the indentation in python is very important
        print("The year is a leap year")
    else:
        print("The year is not a leap year")

# WAP in Python to print signal post
def block5():   
    a=int(input("Enter the signal color : "))
    if a==(red):
        print("Stop")
    elif (a==yellow):
        print("Slow down")
    elif (a==green):
        print("Go ahead")
    else:
        print("Invalid input")

if __name__ == "__main__":
    block1()   # Run only this