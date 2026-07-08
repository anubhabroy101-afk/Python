# WAP in python to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
n = int(input("Pat-1: Enter the number of rows: "))
for i in range(1, n+1):
    print("* " * i)  # This will print "* " i times in each row
