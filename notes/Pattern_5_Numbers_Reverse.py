# WAP in python to print the following pattern⭐
# 12345
# 1234
# 123
# 12
# 1
a = int(input("Pat-5: Enter the number of row : "))
for i in range(a, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
    print()
