#WAP to find all prime numbers in a given range
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print("Prime numbers between", a, "and", b, "are:")
for i in range(a, b + 1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        if i > 1:
            print("{i}, ", end=" ")