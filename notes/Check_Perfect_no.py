#WAP in Python to check whether a number is perfect or not.

a = int(input("Enter a number: "))
b = int(a/2)
sum = 0
for i in range(1, b + 1):
    if a % i == 0:
        sum += i

if sum == a:
    print("The number is perfect.")
else:
    print("The number is not perfect.")