#WAP in python to print the following pattern
#        *
#      * *
#    * * *
#  * * * *
#* * * * *
print("Method 1:")
n = int(input("Enter the number of rows: "))
for i in range (n):
    for j in range (2*(n-i-1)):
        print(" ", end="")
    for k in range (i+1):
        print(" *", end="")
    print()

print("Method 2:")
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
