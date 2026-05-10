# Entry controlled loop:
    # 1 for loop:
        #Syntax:
        # for variable in range(lower lim, upper lim, increment/decrement):
    # 2 while loop:
# Exit controoled loop:
    # 3 Do while loop

def block1():  # WAP in Python to add all no in a range
    print(1)
    a = int(input("Enter the lower limit : "))
    b = int(input("Enter the upper limit : "))
    s = 0
    for i in range(a, b+1):
        s = s+i
    print("The sum of all numbers in the range is : ", s)

def block2():  # WAP in Python to find the even no in a range
    print(2)
    a = int(input("Enter the lower limit : "))
    b = int(input("Enter the upper limit : "))
    print("The even numbers in the range are : ")
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)

def block3():  # WAP in Python to find all the even no between 1 to 100
    print(3)
    print("The even numbers between 1 and 100 are : ")
    for i in range(2, 101, 2):
        print(i)

def block4():# WAP in Python to find all the prime no with in a range
    print(4)
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
    print(5)
    a = int(input("Enter the number : "))
    fac = 1
    for i in range(1, a+1):
        fac = fac*i
    print("The factorial of the number is : ", fac)

def block6():  # WAP in Python to check weather a no is palindrome or not
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

def block7():  # WAP in Python to check weather a no is armstrong or not
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

def block8():# WAP in Python to check if a no in krishnamurthy or not
    # 145 = 1! + 4! + 5!
    print(8)
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

def block9():
    #WAP in Python to calculate the following 
    # 1² + 2³ + 3⁴ +...+ n^(n+1)
    print(9)
    n = int(input("Enter the number of terms: "))
    s = 0
    for i in range(1, n+1):
        s = s + (i ** (i+1))
    print("The sum of the series is: ", s)

if __name__ == "__main__":
    block9()   # Run only this
    #block2()   # Run this also