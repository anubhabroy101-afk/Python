#WAP in Python to print a hollow diamond pattern
n = int(input("Enter the no of rows: "))
m = int((n+1)/2)
for i in range(1,n+1):
    print(' ' * abs(m-i) + '* ' + '  ' * (((m-2) - abs(m-i)) if (2<i<n-1)else(0)) + "*" if (1<i<n) else (' ' * abs(m-i) + '* ') )