"""
==============================================================
CHAPTER 2: INPUT, OUTPUT & FORMATTING
==============================================================
User interaction layer
- print() function
- input() function
- Escape sequences
- Text formatting
==============================================================
"""

# ============ print() FUNCTION ============
# Used to display output to console

print("Hello, World!")
print("Python", "Programming", "Language")

# print() parameters:
# - sep: separator between multiple values (default: space)
# - end: character at end of line (default: newline)

print("A", "B", "C", sep="-")  # Output: A-B-C
print("Line1", end=" ")
print("Line2")  # Output: Line1 Line2

# Multiple print statements
print("First line")
print("Second line")
print("Third line")

# ============ input() FUNCTION ============
# Takes user input from keyboard (returns as string)

"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old")
"""

# ============ ESCAPE SEQUENCES ============
# Special characters for formatting

print("\n--- ESCAPE SEQUENCES ---")

# \n = newline
print("Line 1\nLine 2\nLine 3")

# \t = tab (horizontal spacing)
print("Name\tAge\tCity")
print("Alice\t25\tNew York")
print("Bob\t30\tLondon")

# \r = carriage return
print("Hello\rWorld")  # Output: World (overwrites Hello)

# \\ = backslash
print("Path: C:\\Users\\Documents\\file.txt")

# \" and \' = quotes
print("He said \"Hello\"")
print('She said "Hi"')
print("It's a beautiful day")

# \b = backspace
print("Hello\bWorld")  # Removes 'o'

# \0 = null character
print("Hello\0World")

# ============ TEXT FORMATTING ============

print("\n--- TEXT FORMATTING METHODS ---")

# 1. Using concatenation
name = "Alice"
age = 25
print("Name: " + name + ", Age: " + str(age))

# 2. Using format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# 3. Using f-strings (Python 3.6+) - RECOMMENDED
print(f"Name: {name}, Age: {age}")
print(f"Next year age: {age + 1}")

# ============ FORMATTING NUMBERS ============

num = 3.14159
print(f"Number: {num}")
print(f"2 decimal places: {num:.2f}")  # 3.14
print(f"4 decimal places: {num:.4f}")  # 3.1416

# Scientific notation
large_num = 1234567890
print(f"Scientific: {large_num:.2e}")  # 1.23e+09

# Percentage
percentage = 0.85
print(f"Percentage: {percentage:.1%}")  # 85.0%

# ============ STRING ALIGNMENT & PADDING ============

text = "Python"
print(f"Left align (10 chars): '{text:<10}'")  # 'Python    '
print(f"Right align (10 chars): '{text:>10}'")  # '    Python'
print(f"Center align (10 chars): '{text:^10}'")  # '  Python  '

# Padding with zeros
num = 42
print(f"Zero padded: {num:05d}")  # 00042

# ============ COMPLEX FORMATTING EXAMPLE ============

print("\n--- INVOICE FORMAT ---")
items = [
    ("Laptop", 1, 899.99),
    ("Mouse", 2, 25.50),
    ("Keyboard", 1, 79.99)
]

print(f"{'Item':<15} {'Qty':>5} {'Price':>10} {'Total':>10}")
print("-" * 45)

total = 0
for item, qty, price in items:
    item_total = qty * price
    total += item_total
    print(f"{item:<15} {qty:>5} ${price:>9.2f} ${item_total:>9.2f}")

print("-" * 45)
print(f"{'TOTAL':<15} {'':<5} {'':<10} ${total:>9.2f}")

# ============ MULTIPLE OUTPUT FORMATS ============

print("\n--- DIFFERENT OUTPUT FORMATS ---")

# Binary representation
num = 10
print(f"Binary: {num:b}")  # 1010
print(f"Binary (0b prefix): {bin(num)}")  # 0b1010

# Octal representation
print(f"Octal: {num:o}")  # 12
print(f"Octal (0o prefix): {oct(num)}")  # 0o12

# Hexadecimal representation
print(f"Hex: {num:x}")  # a
print(f"Hex (0x prefix): {hex(num)}")  # 0xa

# ============ DISPLAYING DATA STRUCTURES ============

print("\n--- DISPLAYING COMPLEX DATA ---")

student_info = {
    "name": "Bob",
    "age": 22,
    "marks": [85, 90, 78]
}

# Pretty printing with indentation
import json
print("Using json.dumps():")
print(json.dumps(student_info, indent=2))

# ============ OUTPUT COLOR & FORMATTING (Optional) ============

print("\n--- TEXT STYLING (Using ANSI Codes) ---")
# Note: Works in most terminals

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

print(f"{RED}This is red text{END}")
print(f"{GREEN}This is green text{END}")
print(f"{BOLD}This is bold text{END}")
print(f"{BLUE}{BOLD}Blue and Bold{END}")

# ============ PRACTICE EXAMPLES ============

print("\n--- PRACTICE EXAMPLES ---")

# Example 1: Display a simple receipt
product = "Headphones"
price = 49.99
quantity = 2
discount = 0.1

subtotal = price * quantity
discount_amount = subtotal * discount
final_total = subtotal - discount_amount

print(f"\n{'Product':<20} {product}")
print(f"{'Price':<20} ${price:.2f}")
print(f"{'Quantity':<20} {quantity}")
print(f"{'Subtotal':<20} ${subtotal:.2f}")
print(f"{'Discount (10%)':<20} -${discount_amount:.2f}")
print(f"{'Final Total':<20} ${final_total:.2f}")

# Example 2: Matrix display
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix:")
for row in matrix:
    print(" ".join(f"{val:3d}" for val in row))
