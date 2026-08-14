#WAp in Python to print a Square "L"
# *
# *
# * * *

n = int(input("Enter the no of rows: "))
for i in range(1, n + 1):
    print("* " * (1 if i < n else n))