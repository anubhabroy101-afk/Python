# WAP in Python to print all the even no in a list
n = int(input("#3:- \nEnter the number of elements: "))
a = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print("The list is:", a)
print("Even numbers in the list are:")
for i in a:
    if i % 2 == 0:
        print(i, end=" ")
