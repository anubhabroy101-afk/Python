#WAP in python to create a list of Krishna murti and armstrong nos from a given range
def kr(a):
    s,kr=0,a
    while a>0:
        rem=a%10
        f=1
        for i in range(1,rem+1):
            f*=i    
        s+=f
        a//=10
    if kr==s:
        return True
    else:
        return False

def ar(a):
    s,ar=0,a
    while a>0:
        rem=a%10
        s+=rem**3
        a//=10
    if s==ar:
        return True
    else:
        return False
    
a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
kr_list=[]
arm_list=[]
for i in range(a,b+1):
    if kr(i):
        kr_list.append(i)
    if ar(i):
        arm_list.append(i)  

print("Krishna Murti numbers in the given range are: ",kr_list)
print("Armstrong numbers in the given range are: ",arm_list)
