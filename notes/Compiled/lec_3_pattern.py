# 1 WAP in python to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
def block1():
    n = int(input("Pat-1: Enter the number of rows: "))
    for i in range(1, n+1):
        print("* " * i)  # This will print "* " i times in each row

# 2 WAP in python to print the following pattern
# * * * *
# * * *
# * *
# *


def block2():
    n = int(input("Enter the number of rows: "))
    for i in range(n, 0, -1):
        print("* " * i)

# 3 WAP in python to print the following pattern
# 1
# 12
# 123
# 1234
# 12345


def block3():
    a = int(input("Pat-3: Enter the number of row : "))
    for i in range(1, a+1):
        for j in range(1, i+1):
            print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
        print()

# 4 WAP in python to print the following pattern
# 54321
# 4321
# 321
# 21
# 1

def block4():
    a = int(input("Pat-4: Enter the number of row : "))
    for i in range(a, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
        print()

# 4 WAP in python to print the following pattern⭐
# 12345
# 1234
# 123
# 12
# 1


def block5():
    a = int(input("Pat-5: Enter the number of row : "))
    for i in range(a, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")# end=" " is used to print the numbers in the same line with a space in between
        print()

# 5 WAP in python to print the following pattern⭐
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


def block6():
    n = int(input("Pat-6: Enter the number of rows: "))
    for i in range(1, n+1):
        print(" " * (n - i) + "* " * i)# " " * (n - i) is used to print the spaces before the stars to create the right alignment

# 5 WAP in python to print the following pattern ⭐⭐
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


def block7():
    n = int(input("PAT-7: Enter the upper limit: "))
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

# 6 WAP in python to print the following pattern
#    *
#   **
#  ***
# ****
#*****
def block8():
    n = int(input("Pat-8: Enter the number of rows: "))
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
    block1()   # Run only this
