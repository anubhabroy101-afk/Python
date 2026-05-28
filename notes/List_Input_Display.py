# WAP in Python to take all element as input and display the list
n = int(input("#2:- \nEnter the number of elements: "))
a = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print("The list is:", a)
