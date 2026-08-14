#WAP in Python to print the following pattern
#    1
#  1 2
#1 2 3

n = int(input("Pat-9: Enter the number of rows: "))
for i in range(1, n+1):
    print("  " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))
