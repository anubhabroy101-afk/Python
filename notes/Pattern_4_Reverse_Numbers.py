# WAP in python to print the following pattern
# 54321
# 4321
# 321
# 21
# 1
a = int(input("Pat-4: Enter the number of row : "))
for i in range(a, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
    print()
