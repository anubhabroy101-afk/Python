# WAP in Python to find the even no in a range
print(2)
a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
print("The even numbers in the range are : ")
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)
