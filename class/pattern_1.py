#WAP in Pythonto print the following pattern
#*
#* *
#* * *
#* * * *
#* * * * *

n = int(input("Enter the number of rows: "))

print("Method 1:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("Method 2:")
for i in range(1, n + 1):
    print("* " * i)