# Entry controlled loop
    # 1 for loop
    # 2 while loop
# Exit controoled loop
    # 3 Do while loop

def block1():  # WAP in Python to add all no in a range
    a = int(input("Enter the lower limit : "))
    b = int(input("Enter the upper limit : "))
    s = 0
    for i in range(a, b+1):
        s = s+i
    print("The sum of all numbers in the range is : ", s)


def block2():  # WAP in Python to find the even no in a range
    a = int(input("Enter the lower limit : "))
    b = int(input("Enter the upper limit : "))
    print("The even numbers in the range are : ")
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)


def block3():  # WAP in Python to find all the even no between 1 to 100
    print("The even numbers between 1 and 100 are : ")
    for i in range(2, 101, 2):
        print(i)


def block4():  # WAP in Python to find all the prime no with in a range
    a = int(input("Enter the lower limit : "))
    b = int(input("Enter the upper limit : "))
    print("The prime numbers in the range are : ")
    for i in range(a, b+1):
        k = 0
        for j in range(2, i+1):
            if (i % j == 0):
                k = k+1
        if (k == 1):
            print(i)


def block5():  # WAP in Python to find the factorial of any no.
    a = int(input("Enter the number : "))
    fac = 1
    for i in range(1, a+1):
        fac = fac*i
    print("The factorial of the number is : ", fac)


def block6():  # WAP in Python to check weather a no is palindrome or not
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


def block7():  # WAP in Python to check weather a no is armstrong or not
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

if __name__ == "__main__":
    block7()   # Run only this
    #block2()   # Run this also