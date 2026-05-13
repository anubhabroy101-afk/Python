#WAP in python to print the following pattern
#    *
#   **
#  ***
# ****
n = int(input("Enter the number of rows: "))
for i in range (n):
    for j in range (2*(n-i-1)):
        print(" ", end="")
    for k in range (i+1):
        print(" *", end="")
    print()