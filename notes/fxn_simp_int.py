#WAP in python to find simple interest
def sim_int(a,b,c):
    return (a*b*c)/100

p = int(input("Enter the principle amount: "))
t = int(input("Enter the time period: "))
r = int(input("Enter the rate: "))

i = sim_int(p,t,r)

print("The simpl interest is",i)
