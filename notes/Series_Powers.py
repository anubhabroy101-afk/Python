# WAP in Python to calculate the following 
# 1² + 2³ + 3⁴ +...+ n^(n+1)
print(9)
n = int(input("Enter the number of terms: "))
s = 0
for i in range(1, n+1):
    s = s + (i ** (i+1))
print("The sum of the series is: ", s)
