n = int(input("Enter the no: "))
a = n/2
for i in range(1,n+1):
    p = i*(i+1)
    if(p==n):
        print("The no is pronic")
        break
if(p!=n):
    print("The no is not pronic")
