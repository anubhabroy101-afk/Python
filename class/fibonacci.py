#WAP to find the Fibonacci series
n=int(input("Enter the number of terms: "))
a,b,sum=0,1,0
#list = []
for i in range(n):
    print(a, end=" ")
    # (or) list.append(a)
    sum=a+b
    a=b
    b=sum
#print(list)