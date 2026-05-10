#WAP in python to check if a number is prime or not
print("Methord 1")
n=int (input("Enter the number: ")) 
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

print("Methord 2")
n=int (input("Enter the number: "))
k=0
if n!=1:
    for i in range(2,n):
        if n % i == 0:
            k+=1
if k == 0:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
