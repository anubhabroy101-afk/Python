# WAP in python to print the following pattern
#1 2 3 
#  1 2 
#    1

n = int(input("Pat-11: Enter the number of rows: "))
for i in range(n):
    print("  " * i)
    for j in range(n - i):
        print(j, end=" ")