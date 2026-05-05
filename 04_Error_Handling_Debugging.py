"""
==============================================================
CHAPTER 4: ERROR HANDLING & DEBUGGING
==============================================================
Program correctness and reliability
- Compile-time errors
- Runtime errors
- Logical errors
- Debugging methods
==============================================================
"""

import sys
import traceback

# ============ TYPES OF ERRORS ============

print("=== TYPES OF ERRORS ===\n")

# 1. COMPILE-TIME ERRORS (Syntax Errors)
# These are caught before the program runs
# Example (commented to prevent error):
# x = 10
# y = 20
# print(x y)  # SyntaxError: invalid syntax

# Another syntax error example:
# if x > 5  # SyntaxError: missing colon

print("1. COMPILE-TIME ERRORS (Syntax Errors)")
print("   - Missing colon after if, for, while, etc.")
print("   - Incorrect indentation")
print("   - Unclosed quotes or parentheses")
print("   - Invalid variable names")
print("   - Caught by Python interpreter before execution\n")

# 2. RUNTIME ERRORS (Exceptions)
print("2. RUNTIME ERRORS (Exceptions)")
print("   - Errors that occur during program execution")
print("   - Program crashes if not handled")
print("   - Examples: TypeError, ValueError, ZeroDivisionError\n")

# Examples of runtime errors:

# ZeroDivisionError
print("Example - ZeroDivisionError:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Error: Cannot divide by zero!")

# TypeError
print("\nExample - TypeError:")
try:
    result = "5" + 5
except TypeError:
    print("  Error: Cannot concatenate string and integer!")

# ValueError
print("\nExample - ValueError:")
try:
    num = int("abc")
except ValueError:
    print("  Error: Cannot convert 'abc' to integer!")

# IndexError
print("\nExample - IndexError:")
try:
    lst = [1, 2, 3]
    item = lst[10]
except IndexError:
    print("  Error: Index out of range!")

# KeyError
print("\nExample - KeyError:")
try:
    data = {"name": "Alice", "age": 25}
    value = data["city"]
except KeyError:
    print("  Error: Key 'city' not found in dictionary!")

# AttributeError
print("\nExample - AttributeError:")
try:
    num = 42
    result = num.upper()
except AttributeError:
    print("  Error: Integer has no method 'upper'!")

# ============ LOGICAL ERRORS ============
print("\n3. LOGICAL ERRORS")
print("   - Code runs without errors but produces wrong results")
print("   - Hardest to find and fix")
print("   - Requires careful testing\n")

# Example of logical error
print("Example - Logical Error:")
# Wrong formula for average
marks = [80, 90, 85]
# incorrect_avg = sum(marks) + len(marks)  # Wrong!
correct_avg = sum(marks) / len(marks)  # Correct
print(f"  Correct average: {correct_avg}")

# Another logical error example
print("\nAnother Example - Logical Error:")
# Trying to find maximum of two numbers incorrectly
a = 10
b = 20
# wrong_max = max(a, b)  # This is correct
# But if we did: wrong_max = a if a > b else b  # Correct
# vs: wrong_max = a if a < b else b  # Logical error!

# ============ DEBUGGING METHODS ============
print("\n=== DEBUGGING METHODS ===\n")

# 1. Print Debugging
print("1. PRINT DEBUGGING (Print Statements)")
x = 10
y = 20
print(f"  Value of x: {x}")
print(f"  Value of y: {y}")
print(f"  Sum: {x + y}\n")

# 2. Tracing Code
print("2. TRACING CODE")
def calculate(a, b):
    print(f"  Entering calculate with a={a}, b={b}")
    result = a + b
    print(f"  Calculated result: {result}")
    return result

result = calculate(5, 3)
print(f"  Final result: {result}\n")

# 3. Using assert statements
print("3. USING ASSERT STATEMENTS")
def divide(a, b):
    assert b != 0, "Divisor cannot be zero!"
    return a / b

try:
    print(f"  10 / 2 = {divide(10, 2)}")
    print(f"  10 / 0 = {divide(10, 0)}")  # Will trigger assertion
except AssertionError as e:
    print(f"  Assertion failed: {e}\n")

# 4. Error Messages
print("4. USING ERROR MESSAGES")
def get_age(age_str):
    try:
        age = int(age_str)
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    except ValueError as e:
        print(f"  Error: {e}")
        return None

age = get_age("-5")
print()

# ============ USING try-except-finally ============
print("=== USING TRY-EXCEPT-FINALLY ===\n")

# 1. Simple try-except
print("1. Simple try-except:")
try:
    num = int("hello")
except ValueError:
    print("  Cannot convert 'hello' to integer\n")

# 2. Multiple except blocks
print("2. Multiple except blocks:")
def risky_operation(operation_type):
    try:
        if operation_type == "divide":
            return 10 / 0
        elif operation_type == "type":
            return "5" + 5
        elif operation_type == "index":
            return [1, 2, 3][10]
    except ZeroDivisionError:
        print("  Caught: Division by zero")
    except TypeError:
        print("  Caught: Type mismatch")
    except IndexError:
        print("  Caught: Index error")
    except Exception as e:
        print(f"  Caught: Unknown error - {e}")

risky_operation("divide")
risky_operation("type")
risky_operation("index")
print()

# 3. try-except-finally
print("3. try-except-finally:")
def file_operation():
    try:
        print("  Opening file...")
        # file = open("nonexistent.txt")
        print("  Reading file...")
        return "File content"
    except FileNotFoundError:
        print("  File not found!")
        return None
    finally:
        print("  Cleanup: Closing file...\n")

result = file_operation()

# ============ RAISING EXCEPTIONS ============
print("=== RAISING EXCEPTIONS ===\n")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age is valid: {age}"

print("1. Raising custom exceptions:")
try:
    print(f"  {validate_age(25)}")
except (TypeError, ValueError) as e:
    print(f"  Error: {e}")

try:
    print(f"  {validate_age(-5)}")
except (TypeError, ValueError) as e:
    print(f"  Error: {e}")

try:
    print(f"  {validate_age('25')}")
except (TypeError, ValueError) as e:
    print(f"  Error: {e}\n")

# ============ DEBUGGING WITH sys.exc_info() ============
print("=== DEBUGGING WITH sys.exc_info() ===\n")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Exception type: {exc_type.__name__}")
    print(f"Exception value: {exc_value}")
    print(f"Traceback: {exc_traceback}\n")

# ============ STACK TRACE ============
print("=== STACK TRACE ===\n")

def func_a():
    return func_b()

def func_b():
    return func_c()

def func_c():
    return 10 / 0

try:
    result = func_a()
except ZeroDivisionError:
    print("Stack trace:")
    traceback.print_exc()

# ============ BEST PRACTICES ============
print("\n=== BEST PRACTICES FOR ERROR HANDLING ===")
print("""
1. Be specific with exceptions:
   DON'T: except:
   DO: except ValueError:

2. Always use finally for cleanup:
   try:
       do_something()
   finally:
       cleanup()

3. Use meaningful error messages:
   raise ValueError(f"Age {age} is invalid")

4. Don't ignore exceptions silently:
   except:
       pass  # BAD!
   except SomeError as e:
       print(f"Error: {e}")  # Good

5. Test edge cases:
   - Empty inputs
   - Negative numbers
   - Very large numbers
   - None values

6. Debug systematically:
   - Add print statements
   - Use assertions
   - Check variable values
   - Read error messages carefully
""")
