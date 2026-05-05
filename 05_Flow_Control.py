"""
==============================================================
CHAPTER 5: FLOW CONTROL (PROGRAM DECISION MAKING)
==============================================================
Controls execution order

A. Basic Flow Concepts
- Sequential flow
- Conditional flow
- Iterative flow
- Indentation

B. Conditional Statements
- if, else, elif
- Logical operators in conditions

C. Loops (Iteration)
- for loop
- while loop
- range()
- break, continue, else
- Nested loops

==============================================================
"""

# ============ SEQUENTIAL FLOW ============
print("=== SEQUENTIAL FLOW ===\n")

# Code executes line by line from top to bottom
a = 10
print(f"Step 1: a = {a}")

b = 20
print(f"Step 2: b = {b}")

c = a + b
print(f"Step 3: c = a + b = {c}\n")

# ============ INDENTATION ============
print("=== INDENTATION (CRUCIAL IN PYTHON) ===\n")

# Python uses indentation to define code blocks
# Indentation determines scope

x = 5
if x > 0:
    print("  x is positive (indented inside if block)")
    print("  This is still inside the if block")

print("This is outside the if block (back to normal indentation)\n")

# ============ CONDITIONAL FLOW - if, else, elif ============
print("=== CONDITIONAL STATEMENTS ===\n")

# 1. Simple if statement
print("1. Simple if statement:")
age = 18
if age >= 18:
    print("  You are an adult\n")

# 2. if-else statement
print("2. if-else statement:")
score = 45
if score >= 50:
    print("  Pass")
else:
    print("  Fail\n")

# 3. if-elif-else statement
print("3. if-elif-else statement:")
marks = 85
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"  Marks: {marks}, Grade: {grade}\n")

# 4. Nested if statements
print("4. Nested if statements:")
user_age = 25
user_has_license = True

if user_age >= 18:
    if user_has_license:
        print("  Allowed to drive\n")
    else:
        print("  Need to get license\n")
else:
    print("  Too young to drive\n")

# 5. Ternary operator (conditional expression)
print("5. Ternary operator (one-line if-else):")
temperature = 30
weather = "Hot" if temperature > 25 else "Cold"
print(f"  Temperature: {temperature}°C, Weather: {weather}\n")

# ============ ITERATIVE FLOW - LOOPS ============
print("=== LOOPS (ITERATION) ===\n")

# 1. for loop - fixed iterations
print("1. for loop (fixed iterations):")
print("  Printing numbers 1 to 5:")
for i in range(1, 6):
    print(f"    {i}")
print()

# 2. range() function
print("2. Understanding range():")
print("  range(5):", list(range(5)))  # 0, 1, 2, 3, 4
print("  range(1, 6):", list(range(1, 6)))  # 1, 2, 3, 4, 5
print("  range(0, 10, 2):", list(range(0, 10, 2)))  # 0, 2, 4, 6, 8
print("  range(10, 0, -1):", list(range(10, 0, -1)))  # 10, 9, 8, ..., 1
print()

# 3. for loop - iterate through list
print("3. for loop with lists:")
fruits = ["apple", "banana", "cherry"]
print("  Fruits:")
for fruit in fruits:
    print(f"    {fruit}")
print()

# 4. for loop with enumerate
print("4. for loop with enumerate (index + value):")
for index, fruit in enumerate(fruits):
    print(f"    {index}: {fruit}")
print()

# 5. while loop - conditional iterations
print("5. while loop (conditional iterations):")
count = 1
print("  Counting from 1 to 5:")
while count <= 5:
    print(f"    {count}")
    count += 1
print()

# 6. break statement - exit loop early
print("6. break statement (exit loop early):")
print("  Finding first number divisible by 7:")
for num in range(1, 20):
    if num % 7 == 0:
        print(f"    Found: {num}")
        break
print()

# 7. continue statement - skip current iteration
print("7. continue statement (skip iteration):")
print("  Printing odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"    {num}")
print()

# 8. else clause with loops
print("8. else clause with loops:")
print("  (else runs when loop completes normally)")
print("  Loop that completes:")
for i in range(1, 4):
    print(f"    Iteration {i}")
else:
    print("    Loop completed successfully!")
print()

print("  Loop with break (else doesn't run):")
for i in range(1, 10):
    if i == 3:
        break
    print(f"    Iteration {i}")
else:
    print("    This won't print because we broke out\n")

# 9. Nested loops
print("9. Nested loops (loop inside loop):")
print("  Multiplication table (1-3 x 1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"    {i} × {j} = {i*j}")
print()

# ============ LOOP EXAMPLES ============
print("=== PRACTICAL LOOP EXAMPLES ===\n")

# Example 1: Sum of numbers
print("Example 1: Sum of numbers from 1 to 100")
total = 0
for num in range(1, 101):
    total += num
print(f"  Sum: {total}\n")

# Example 2: Factorial
print("Example 2: Calculate factorial of 5")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"  5! = {factorial}\n")

# Example 3: Pattern printing
print("Example 3: Print pyramid pattern")
for i in range(1, 6):
    print("  " + "*" * i)
print()

# Example 4: Pattern printing (numbers)
print("Example 4: Print number pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}", end=" ")
    print()
print()

# Example 5: Find prime numbers
print("Example 5: Prime numbers from 2 to 20")
print("  ", end="")
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num}", end=" ")
print("\n")

# Example 6: String reversal
print("Example 6: Reverse a string")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"  Original: {text}")
print(f"  Reversed: {reversed_text}\n")

# Example 7: Count occurrences
print("Example 7: Count character occurrences")
text = "programming"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"  Text: {text}")
print(f"  Character count: {char_count}\n")

# ============ WHILE LOOP EXAMPLES ============
print("=== WHILE LOOP EXAMPLES ===\n")

# Example 1: User input validation
print("Example 1: Input validation (commented)")
"""
age = -1
while age < 0 or age > 120:
    age = int(input("Enter valid age (0-120): "))
print(f"Valid age: {age}")
"""

# Example 2: Countdown
print("Example 2: Countdown")
count = 5
while count > 0:
    print(f"  {count}")
    count -= 1
print("  Blastoff!\n")

# Example 3: Keep asking until correct answer
print("Example 3: Guess the number (commented)")
"""
secret = 7
guess = None
attempts = 0
while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"Correct! It took {attempts} attempts")
"""

# ============ COMMON MISTAKES ============
print("=== COMMON MISTAKES ===")
print("""
1. FORGETTING COLON after if/for/while:
   ❌ if x > 5
   ✓ if x > 5:

2. WRONG INDENTATION:
   ❌ if x > 5:
   print(x)  # Not indented
   ✓ if x > 5:
       print(x)  # Properly indented

3. OFF-BY-ONE ERROR in range:
   ❌ for i in range(1, 11)  # Goes 1-10
       print(i)
   ✓ for i in range(1, 11)  # Correct - includes 10

4. INFINITE LOOP:
   ❌ while True:
       print(x)  # No break or condition change!
   ✓ while x < 10:
       print(x)
       x += 1

5. COMPARING WITH == vs =:
   ❌ if x = 5:  # Assignment, not comparison
   ✓ if x == 5:  # Comparison
""")
