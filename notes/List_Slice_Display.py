# WAP in Python to take all element as input and display from 3rd to7th element
n = int(input("#4:- \nEnter the number of elements: "))
a = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print("The list is:", a)
p = int(input("Enter the initial element: "))
q = int(input("Enter the final element: "))
c = a[p:q] #[p-1:q+1] if we want to include the qth element as well
print("The list from element no. {p} to {q} is: ", c)
