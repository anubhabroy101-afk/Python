#WAP in Python to to find the value of: 1/1!+2/2!+3/3!+...+n/n!
def pat(a):
    val = 0
    f = 1
    for i in range(1,a+1):
        f *= i
        val += i/f
    return val

print("Find the value of: 1/1!+2/2!+3/3!+...+n/n!")

x = int(input("Enter the no of term: "))
y = pat(x)
print("The value till",x,"terms is",y)
