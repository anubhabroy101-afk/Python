#WAP in Python to find perfect numbers in a given range.
def perfect_number(n):
    b = int(n/2)
    sum = 0
    for i in range(1, b + 1):
        if n % i == 0:
            sum += i
    return sum == n #True if the number is perfect, False otherwise.

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))

print("Perfect numbers in the given range are:")
for i in range(a, b + 1):
    if perfect_number(i):
        print(i)