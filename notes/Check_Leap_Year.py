# WAP to check a leap year
y=int(input("Enter the year : "))
if (y%4==0 and y%100!=0) or (y%400==0): #Keep in mind that the indentation in python is very important
    print("The year is a leap year")
else:
    print("The year is not a leap year")
