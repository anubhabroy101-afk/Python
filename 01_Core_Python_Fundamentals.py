"""
==============================================================
CHAPTER 1: CORE PYTHON FUNDAMENTALS (BASICS & SETUP)
==============================================================
Foundation — must be learned first
- Python Source Code, Byte Code, PVM, Frozen Binary
- Installing Python IDLE
- Modes of Python IDLE
- Components of a Python Program
- Data Types
- Variables
- Expressions & Statements
- L-Value and R-Value
- Comments
- Writing simple code
==============================================================
"""

# ============ COMMENTS ============
# This is a single-line comment (used for explanations)
"""
This is a multi-line comment (docstring)
Used for documentation and detailed explanations
Can span multiple lines
"""

# ============ COMPONENTS OF A PYTHON PROGRAM ============
# 1. Literals (fixed values)
literal_int = 10
literal_float = 3.14
literal_string = "Hello Python"
literal_bool = True

# 2. Variables (containers for values)
name = "Anubhab"
age = 20
gpa = 3.85
is_student = True

# ============ DATA TYPES ============
# Python has several built-in data types

# 1. INTEGER - Whole numbers
num_int = 42
print(f"Integer: {num_int}, Type: {type(num_int)}")

# 2. FLOAT - Decimal numbers
num_float = 3.14159
print(f"Float: {num_float}, Type: {type(num_float)}")

# 3. STRING - Text
text = "Python Programming"
print(f"String: {text}, Type: {type(text)}")

# 4. BOOLEAN - True or False
is_valid = True
print(f"Boolean: {is_valid}, Type: {type(is_valid)}")

# 5. COMPLEX - Complex numbers
complex_num = 3 + 4j
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# ============ VARIABLES & NAMING CONVENTIONS ============
# Python naming rules:
# - Must start with letter or underscore
# - Can contain letters, digits, underscores
# - Case-sensitive
# - No spaces

valid_name = "Good"
_private_var = "Convention"
age2 = 25

# L-VALUE vs R-VALUE
# L-Value (Left): Variable that receives value (memory location)
# R-Value (Right): Value being assigned

x = 10  # 'x' is L-Value (left), '10' is R-Value (right)
y = x   # 'y' is L-Value, 'x' is R-Value

# ============ EXPRESSIONS & STATEMENTS ============
# Expression: Code that evaluates to a value
expression_result = 2 + 3 * 4  # Expression evaluates to 14

# Statement: Complete instruction (may or may not return value)
message = "This is a statement"

# ============ PYTHON MODES ============
"""
INTERACTIVE MODE (Python IDLE Shell):
- Type commands one at a time
- Results display immediately
- Good for learning and testing small code
- Starts when you open Python IDLE or type 'python' in terminal

SCRIPT MODE:
- Write complete program in .py file
- Run entire file at once
- Good for larger programs
- Requires saving and running file
"""

# ============ PYTHON ARCHITECTURE ============
"""
SOURCE CODE (.py file)
         ↓
    Python Compiler
         ↓
   BYTE CODE (.pyc file)
         ↓
  Python Virtual Machine (PVM)
         ↓
    MACHINE EXECUTABLE

Frozen Binary:
- Compiled Python bytecode packaged into single executable
- Used in deployment (PyInstaller)
"""

# ============ TYPE CONVERSION ============
# Converting between data types

str_num = "25"
int_num = int(str_num)  # String to Integer
print(f"String '{str_num}' converted to Integer: {int_num}")

num = 42
str_converted = str(num)  # Integer to String
print(f"Integer {num} converted to String: '{str_converted}'")

float_num = float("3.14")  # String to Float
print(f"String '3.14' converted to Float: {float_num}")

# ============ SIMPLE PROGRAM EXAMPLE ============
print("\n=== SIMPLE PROGRAM ===")
student_name = "Alice"
student_marks = 95
percentage = (student_marks / 100) * 100

print(f"Student: {student_name}")
print(f"Marks: {student_marks}")
print(f"Percentage: {percentage}%")

# ============ MEMORY & OBJECT ID ============
# Every object has an identity (memory address)
var_a = [1, 2, 3]
var_b = var_a
var_c = [1, 2, 3]

print(f"\nvar_a id: {id(var_a)}")
print(f"var_b id: {id(var_b)}")  # Same as var_a
print(f"var_c id: {id(var_c)}")  # Different from var_a

print(f"var_a is var_b: {var_a is var_b}")  # True (same object)
print(f"var_a is var_c: {var_a is var_c}")  # False (different objects)
print(f"var_a == var_c: {var_a == var_c}")  # True (same content)
