#WAP in Python to find square of a inputed number
def sq(a):
    return a**2

a = [-2,-1,0,1,2]
for i in a:
    print("Square of",i,"is",sq(i))

x = int(input("Enter the no: "))
y = sq(x)
print("Square of",x,"is",y)
