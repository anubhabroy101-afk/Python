# WAP in Python to print all +ve, -ve and 0 in a list
n = int(input("#5:- \nEnter the number of elements: "))
a = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print("The list is:", a)
print("Positive numbers in the list are:")
for i in a:
    if i > 0:
        print(i, end=" ")
print("\nNegative numbers in the list are:")
for i in a:
    if i < 0:
        print(i, end=" ")
print("\nZeroes in the list are:")
for i in a:
    if i == 0:
        print(i, end=" ")
