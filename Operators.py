# Arithmetic operators

a = 10
b = 3
print("Given a =", a, "and b =", b)
print("Arithmetic Operators:")
print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Modulus: a % b =", a % b)  # returns the remainder of the division
print("Exponentiation: a ** b =", a ** b)  # returns a raised to the power of b
print("Floor Division: a // b =", a // b) # returns the quotient of the division, rounded down to the nearest whole number

# Relational & Comparison operators

print("\nRelational & Comparison Operators:")
# returns True if a and b are equal, otherwise returns False
print("Equal: a == b =", a == b)
# returns True if a and b are not equal, otherwise returns False
print("Not Equal: a != b =", a != b)
# returns True if a is greater than b, otherwise returns False
print("Greater Than: a > b =", a > b)
# returns True if a is less than b, otherwise returns False
print("Less Than: a < b =", a < b)
# returns True if a is greater than or equal to b, otherwise returns False
print("Greater Than or Equal: a >= b =", a >= b)
# returns True if a is less than or equal to b, otherwise returns False
print("Less Than or Equal: a <= b =", a <= b)

# Assignment operators

print("\nAssignment Operators:")
c, d = 2, 5
print("Given c =", c, "and d =", d)
print("Assignment: c = d, c =", c)  # assigns the value of d to c
# adds d to c and assigns the result to c
print("Addition Assignment: c += d, c =", c + d)
# subtracts d from c and assigns the result to c
print("Subtraction Assignment: c -= d, c =", c - d)
# multiplies c by d and assigns the result to c
print("Multiplication Assignment: c *= d, c =", c * d)
# divides c by d and assigns the result to c
print("Division Assignment: c /= d, c =", c / d)
# returns the remainder of the division of c by d and assigns it to c
print("Modulus Assignment: c %= d, c =", c % d)
# raises c to the power of d and assigns the result to c
print("Exponentiation Assignment: c **= d, c =", c ** d)
# returns the quotient of the division of c by d, rounded down to the nearest whole number, and assigns it to c
print("Floor Division Assignment: c //= d, c =", c // d)

# Logical operators

val1=True
val2=False
val3=True
print("\nGiven val1 =", val1, ", val2 =", val2, "and val3 =", val3)
print("\nLogical Operators:")
# returns the second operand if both operands are true, otherwise returns the first operand
print("Logical AND: val1 and val2 =", val1 and val2)
# returns the first operand if it is true, otherwise returns the second operand
print("Logical OR: val1 or val2 =", val1 or val2)
# returns True if the operand is false, otherwise returns False
print("Logical NOT: not val1 =", not val1)
# returns True if both operands are true, otherwise returns False
print("Logical AND: val1 and val3 =", val1 and val3)
#a=10 and b=3
val4=(a>b)
val5=(a<b)
val6=(a==b)or(a>b)
print("val4 (a>b) =", val4, "and val5 (a<b) =", val5)
print("val4 or val5 =", val4 or val5)
print("val4 and val5 =", val4 and val5)
print("val6 (a==b or a>b) =", val6)