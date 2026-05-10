#List:-
    #List is mutable
    #Represented by {}
    #List is executed faster
#Tuple:-
    #Tuple is immutable
    #Represented by ()
    #Tuple is executed slower
#List and Tuple are ordered collection of data

def block1():
    #WAP in Python to print all the elements of a list
    a = [1, 2, 3, 4, 5]
    print("#1:- \nThe list is:", a)

    #WAP in Python to add all the numbers in a list
    a = [1, 2, 3, 4, 5]
    total = sum(a)
    print("Sum of all elements:", total)

    #WAP in Python to find the product of all no within a list
    a = [1, 2, 3, 4, 5]
    prod = 1
    for i in a:
        prod *= i # prod = prod * i
    print("Product of all elements:", prod)

def block2():#WAP in Python to take all element as input and display the list
    n = int(input("#2:- \nEnter the number of elements: "))
    a = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        a.append(element)
    print("The list is:", a)

def block3():#WAP in Python to print all the even no in a list
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

def block4():#WAP in Python to take all element as input and display from 3rd to7th element
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

def block5():#WAP in Python to print all +ve, -ve and 0 in a list
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

if __name__ == "__main__":
    block4()