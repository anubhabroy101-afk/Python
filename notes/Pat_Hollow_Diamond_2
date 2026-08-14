#WAP in Python to print a hollow diamond pattern
n = int(input("Enter the no of rows: "))
n = n if n % 2 != 0 else n - 1  # Ensure n is odd
m = int((n+1)/2)
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * abs(m - i) + "* ")
    else:
        print(" " * abs(m - i) + "* " + "  " * ((m-2) - abs(m-i)) + "*")