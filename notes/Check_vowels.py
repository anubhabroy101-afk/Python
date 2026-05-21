#WAP in Python to check if a character is a vowel or not
c = input("Enter a character: ")
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if c in v:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")