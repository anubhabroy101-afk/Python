# WAP in python to print the following pattern
# 1
# 12
# 123
# 1234
# 12345
a = int(input("Pat-3: Enter the number of row : "))
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
    print()
