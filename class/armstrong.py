n=int(input("Enter a number: ")) #Eg 153, 370, 371, 407 are armstrong numbers
sum=0
arm=n
while n>0:
    digit=n%10
    sum+=digit**3
    n//=10
if arm==sum:
    print(arm,"is an Armstrong number")
else:
    print(arm,"is not an Armstrong number")
