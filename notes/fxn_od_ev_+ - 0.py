#WAP in Python to check odd, even, and signe using function call
def check(a):
    if a%2==0:
        if a>0:
            return print("Even positive")
        elif a<0:
            return print("Even negetive")
        else:
            return print("Zero")
    else:
        if a>0:
            return print("Odd positive")
        elif a<0:
            return print("Odd negetive")

a = [-2,-1,0,1,2]
for i in a:
    print(i,"is",end=" ")
    check(i)

x = int(input("Enter the no: "))
check(x)
