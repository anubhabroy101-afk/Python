# wap in python to create a simple calculator
def sum(a,b):
    return a+b
def dif(a,b):
    return a-b
def pro(a,b):
    return a*b
def qou(a,b):
    return a/b
def rem(a,b):
    return a%b

x = int(input("Enter the the first no: "))
y = int(input("Enter the the second no: "))

s = sum(x,y) 
d = dif(x,y)
p = pro(x,y)
q = qou(x,y)
r = rem(x,y)

print("The sum = ",s)
print("The difference = ",d)
print("The product = ",p)
print("The quotient = ",q)
print("The remainder = ",r)



