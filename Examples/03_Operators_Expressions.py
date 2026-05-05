"""
==============================================================
CHAPTER 3: OPERATORS & EXPRESSIONS
==============================================================
Computation and logic building
- Arithmetic operators
- Relational operators
- Logical operators
- Bitwise operators
- Membership operators
- Operator precedence & associativity
- Identity vs equality
==============================================================
"""

# ============ ARITHMETIC OPERATORS ============
print("=== ARITHMETIC OPERATORS ===")

a = 20
b = 6

print(f"Addition: {a} + {b} = {a + b}")  # 26
print(f"Subtraction: {a} - {b} = {a - b}")  # 14
print(f"Multiplication: {a} * {b} = {a * b}")  # 120
print(f"Division: {a} / {b} = {a / b}")  # 3.333... (float division)
print(f"Floor Division: {a} // {b} = {a // b}")  # 3 (integer division)
print(f"Modulus: {a} % {b} = {a % b}")  # 2 (remainder)
print(f"Exponentiation: {a} ** {b} = {a ** b}")  # 64000000

# Useful: Modulus to check even/odd
num = 15
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# ============ RELATIONAL OPERATORS ============
print("\n=== RELATIONAL OPERATORS ===")

x = 15
y = 10

print(f"{x} > {y}: {x > y}")  # True (greater than)
print(f"{x} < {y}: {x < y}")  # False (less than)
print(f"{x} >= {y}: {x >= y}")  # True (greater than or equal)
print(f"{x} <= {y}: {x <= y}")  # False (less than or equal)
print(f"{x} == {y}: {x == y}")  # False (equal)
print(f"{x} != {y}: {x != y}")  # True (not equal)

# Chained comparison
age = 25
print(f"18 <= {age} < 65: {18 <= age < 65}")  # True

# ============ LOGICAL OPERATORS ============
print("\n=== LOGICAL OPERATORS ===")

# AND operator - returns True if both operands are True
p = True
q = False
print(f"True AND False: {p and q}")  # False
print(f"True AND True: {True and True}")  # True

# OR operator - returns True if at least one operand is True
print(f"True OR False: {p or q}")  # True
print(f"False OR False: {False or False}")  # False

# NOT operator - reverses boolean value
print(f"NOT True: {not p}")  # False
print(f"NOT False: {not q}")  # True

# Logical operators with numbers (short-circuit evaluation)
print(f"5 and 10: {5 and 10}")  # 10 (returns last true value)
print(f"0 or 20: {0 or 20}")  # 20 (returns first true value)

# Real-world example
age = 25
income = 50000
has_credit_card = True

eligible_for_loan = age >= 18 and income >= 30000
print(f"Eligible for loan: {eligible_for_loan}")

# ============ BITWISE OPERATORS ============
print("\n=== BITWISE OPERATORS ===")

# These work on binary representations

a_val = 12  # Binary: 1100
b_val = 7   # Binary: 0111

print(f"a = {a_val} (Binary: {bin(a_val)})")
print(f"b = {b_val} (Binary: {bin(b_val)})")

# AND: 1100 & 0111 = 0100 = 4
print(f"a & b (AND): {a_val & b_val}")  # 4

# OR: 1100 | 0111 = 1111 = 15
print(f"a | b (OR): {a_val | b_val}")  # 15

# XOR: 1100 ^ 0111 = 1011 = 11
print(f"a ^ b (XOR): {a_val ^ b_val}")  # 11

# NOT (complement): ~1100 = -1101 = -13
print(f"~a (NOT): {~a_val}")  # -13

# Left shift: 1100 << 1 = 11000 = 24 (multiply by 2)
print(f"a << 1 (Left shift): {a_val << 1}")  # 24

# Right shift: 1100 >> 1 = 0110 = 6 (divide by 2)
print(f"a >> 1 (Right shift): {a_val >> 1}")  # 6

# ============ ASSIGNMENT OPERATORS ============
print("\n=== ASSIGNMENT OPERATORS ===")

c = 10
print(f"c = {c}")

c += 5  # c = c + 5
print(f"c += 5: {c}")  # 15

c -= 3  # c = c - 3
print(f"c -= 3: {c}")  # 12

c *= 2  # c = c * 2
print(f"c *= 2: {c}")  # 24

c //= 4  # c = c // 4
print(f"c //= 4: {c}")  # 6

c %= 5  # c = c % 5
print(f"c %= 5: {c}")  # 1

# ============ MEMBERSHIP OPERATORS ============
print("\n=== MEMBERSHIP OPERATORS ===")

fruits = ["apple", "banana", "cherry"]

print(f"'apple' in fruits: {'apple' in fruits}")  # True
print(f"'orange' in fruits: {'orange' in fruits}")  # False
print(f"'apple' not in fruits: {'apple' not in fruits}")  # False

# String membership
text = "Hello World"
print(f"'Hello' in text: {'Hello' in text}")  # True
print(f"'xyz' in text: {'xyz' in text}")  # False

# Dictionary membership (checks keys)
person = {"name": "Alice", "age": 25}
print(f"'name' in person: {'name' in person}")  # True
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys, not values)

# ============ IDENTITY VS EQUALITY ============
print("\n=== IDENTITY VS EQUALITY ===")

# Equality (==, !=): Compares VALUES
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 != list2: {list1 != list2}")  # False

# Identity (is, is not): Compares MEMORY LOCATION (object id)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is not list2: {list1 is not list2}")  # True

# Same reference
list3 = list1
print(f"list1 is list3: {list1 is list3}")  # True (same object)

# Identity with None
value = None
print(f"value is None: {value is None}")  # True
print(f"value is not None: {value is not None}")  # False

# ============ OPERATOR PRECEDENCE & ASSOCIATIVITY ============
print("\n=== OPERATOR PRECEDENCE ===")

# Higher precedence = evaluated first
# Precedence (High to Low):
# 1. ** (exponentiation) - Right to Left
# 2. *, /, //, % - Left to Right
# 3. +, - - Left to Right
# 4. <, <=, >, >=, ==, != - Left to Right
# 5. not - Right to Left
# 6. and - Left to Right
# 7. or - Left to Right

print(f"2 + 3 * 4 = {2 + 3 * 4}")  # 14 (not 20)
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")  # 20

print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")  # 512 (right to left: 2^(3^2))
print(f"(2 ** 3) ** 2 = {(2 ** 3) ** 2}")  # 64

print(f"10 - 5 - 2 = {10 - 5 - 2}")  # 3 (left to right)
print(f"10 - (5 - 2) = {10 - (5 - 2)}")  # 7

# Complex expression
result = 10 + 5 * 2 - 3 ** 2 / 3
print(f"10 + 5 * 2 - 3 ** 2 / 3 = {result}")

# With logical operators
x_val = 5
y_val = 10
z_val = 15
result = x_val > 0 and y_val < 20 or z_val == 15
print(f"5 > 0 and 10 < 20 or 15 == 15: {result}")  # True

# ============ OPERATOR CHAINING ============
print("\n=== OPERATOR CHAINING ===")

# Python allows chaining comparisons
a_chain = 5
print(f"1 < 5 < 10: {1 < a_chain < 10}")  # True
print(f"1 < 5 < 3: {1 < a_chain < 3}")  # False

score = 75
print(f"50 <= {score} <= 100: {50 <= score <= 100}")  # True

# ============ PRACTICAL EXAMPLES ============
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Check if number is even and positive
num_check = 15
print(f"{num_check} is even and positive: {num_check > 0 and num_check % 2 == 0}")

# Example 2: Grade assignment
marks = 85
grade = "A" if marks >= 80 else "B" if marks >= 70 else "C"
print(f"Marks: {marks}, Grade: {grade}")

# Example 3: Leap year check
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Year {year} is leap year: {is_leap}")
