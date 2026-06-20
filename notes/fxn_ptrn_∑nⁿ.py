#WAP in Python to to find the value of: 1¹+2²+3³+...+nⁿ
def pat(a):
    val = 0
    for i in range(1,a+1):
        val += i**i
    return val

print("Find the value of: 1¹+2²+3³+...+nⁿ")

x = int(input("Enter the no of term: "))
y = pat(x)
print("The value till",x,"terms is",y)
