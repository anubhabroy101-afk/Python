#WAP in Python to print the following pattern
#* * *
#  * *
#    *

n = int(input("Pat-10: Enter the number of rows: "))
for i in range(n):
    print("  " * i + "* " * (n - i))