#WAP in Python to find the mean of a list of numbers using module
import statistics
n = int(input("Enter the number of elements: "))
a = []
for i in range(n):
    b = int(input("Enter an element: "))
    a.append(b)
mean = statistics.mean(a)
print("The mean of the list is:", mean)