# WAP in python to print the following pattern
#    *
#   **
#  ***
# ****
#*****
n = int(input("Pat-8: Enter the number of rows: "))
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
