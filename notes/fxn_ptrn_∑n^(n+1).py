#WAP in Python to to find the value of: 1²+2³+3⁴+...+n^(n+1)
def pat(a):
    val = 0
    for i in range(1,a+1):
        val += i**(i+1)
    return val

print("Find the value of: 1²+2³+3⁴+...+n^(n+1)")

x = int(input("Enter the no of term: "))
y = pat(x)
print("The value till",x,"terms is",y)
