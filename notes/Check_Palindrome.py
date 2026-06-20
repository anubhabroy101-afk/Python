# WAP in Python to check weather a no is palindrome or not
print(6)
a = int(input("Enter the number : "))
pal = a
rev = 0
while (a > 0):
    d = a % 10
    rev = rev*10+d
    a = a//10
if (pal == rev):
    print("The number is a palindrome ✅")
else:
    print("The number is not a palindrome")
