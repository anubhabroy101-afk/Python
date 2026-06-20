#WAP in Python to check signe using function call
def check(a):
    if(a>0):
        return print("Positive")
    elif(a<0):
        return print("Negetive")
    else:
        return print("Zero")

a = [-2,-1,0,1,2]
for i in a:
    print(i,"is",end=" ")
    check(i)
    
x = int(input("Enter the no: "))
check(x)
