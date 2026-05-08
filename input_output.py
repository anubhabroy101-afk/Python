import math
# input
name = input("Enter your name: ")  # this is string input (Default)
age = int(input("Enter your age: "))  # this is integer input
marks = float(input("Enter your marks: "))  # this is float input
# output
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# Practice
# 1. WAP to take two numbers as input and print their sum.

print("Welcome to the sum calculator!")
print("Enter two numbers to find their sum:")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("The sum of", num1, "and", num2, "is", num1 + num2)

# 2. WAP to find the area of a square given the length of its side as input.

print("Welcome to the area calculator for a square!")
a = int(input("Enter the length of the side of the square: "))
print("The area of the square is (using multiplication):", a * a)
print("The area of the square is (using exponentiation):", a ** 2)
print("The area of the square is (using math.pow):", math.pow(a, 2))

# 3. wap to find the average of two numbers given as input.

print("Welcome to the average calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is", average)
