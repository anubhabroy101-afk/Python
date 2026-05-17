# WAP to check if the string is a palindrome
s = input("Enter a string: ")
s = s.replace(" ", "").lower()
if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
