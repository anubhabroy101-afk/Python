# WAP in Python to check if a no in krishnamurthy or not
# 145 = 1! + 4! + 5!
import math

a = int(input("Enter the number : ")) ## Eg: 145, 1, 2, 40585
kri = a
s = 0
while (a > 0):
    d = a % 10
    s = s+math.factorial(d)
    a = a//10  # if we use "/" will give float value
if(kri==s):
    print("The number is a krishnamurthy number ✅")
else:
    print("The number is not a krishnamurthy number")
