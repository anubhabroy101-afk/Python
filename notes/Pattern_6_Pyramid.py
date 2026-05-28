# WAP in python to print the following pattern⭐
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n = int(input("Pat-6: Enter the number of rows: "))
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)# " " * (n - i) is used to print the spaces before the stars to create the right alignment
