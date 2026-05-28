# WAP in Python to add all no in a range
print(1)
a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
s = 0
for i in range(a, b+1):
    s = s+i
print("The sum of all numbers in the range is : ", s)
