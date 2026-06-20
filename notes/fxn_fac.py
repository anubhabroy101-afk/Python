#WAP in python to find factorial using function
def fac(a):
    fac = 1
    for i in range(1,a+1):
        fac*=i
    return fac

x = int(input("Enter the no: "))
z = fac(x)

print("The factorial of",x,"is",z)
