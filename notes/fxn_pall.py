#WAP in python to find palindrom
def pal(a):
    pal = a 
    s = 0
    while(a>0):
        rem = a%10
        s = (s*10) + rem
        a //= 10
    if(pal==s):
        return print(pal,"is a pallindrm no.")
    else:
        return print(pal,"is not a pallindrm no.")

x = int(input("Enter the no: "))

pal(x)
