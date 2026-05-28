# WAP in Python to find all the prime no with in a range
print(4)
a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
print("The prime numbers in the range are : ")
for i in range(a, b+1):
    k = 0
    for j in range(2, i+1):
        if (i % j == 0):
            k = k+1
    if (k == 1):
        print(i)
