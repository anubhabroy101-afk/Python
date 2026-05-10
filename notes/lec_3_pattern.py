#1 WAP in python to print the following pattern 
#*
#* *
#* * *
#* * * *
#* * * * *
def block1(): 
    n = int(input("Enter the number of rows: "))
    for i in range(1, n+1):
        print("* " * i) # This will print "* " i times in each row

#2 WAP in python to print the following pattern
#* * * *
#* * *
#* *
#*
def block2():
    n = int(input("Enter the number of rows: "))
    for i in range(n, 0, -1):
        print("* " * i) # This will print "* " i times in each row

if __name__ == "__main__":
    block1()   # Run only this