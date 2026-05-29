#WAP in Python to print the multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)