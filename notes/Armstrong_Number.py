# WAP in Python to check weather a no is armstrong or not
# 153 = 1³ + 5³ + 3³
print(7)
import math

a = int(input("Enter the number : ")) ## Eg: 135, 370, 1637
arm = a
s = 0
while (a > 0):
    d = a % 10
    s = s+math.pow(d, 3)
    a = a//10  # if we use "/" will give float value
if(arm==s):
    print("The number is an armstrong number ✅")
else:
    print("The number is not an armstrong number")
