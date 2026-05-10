#WAP to check if a number is a palindrome
n=int(input("Enter a number: "))
pal=n
rev=0
while pal>0:
    d=pal%10
    rev=rev*10+d
    pal//=10
if n==rev:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")