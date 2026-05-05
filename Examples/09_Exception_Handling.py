"""
==============================================================
CHAPTER 9: EXCEPTION HANDLING (ADVANCED ERROR CONTROL)
==============================================================
Runtime error management

- try-except
- Specific exceptions
- else, finally

Note: Difference from Chapter 4:
- Chapter 4 = Types of errors (what can go wrong)
- Chapter 9 = Handling errors in code (what to do about them)

==============================================================
"""

import sys
import traceback
from typing import Union

# ============ TRY-EXCEPT BASICS ============
print("=== TRY-EXCEPT BASICS ===\n")

# 1. Basic try-except
print("1. Basic try-except:")
try:
    num = int("not a number")
except ValueError:
    print("  Caught: Cannot convert to integer\n")

# 2. Accessing exception info
print("2. Accessing exception information:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Exception type: {type(e).__name__}")
    print(f"  Exception message: {e}\n")

# 3. Multiple except blocks
print("3. Multiple except blocks:")
def risky_operation(operation_type):
    try:
        if operation_type == "divide":
            return 10 / 0
        elif operation_type == "convert":
            return int("abc")
        elif operation_type == "index":
            return [1, 2, 3][10]
    except ZeroDivisionError:
        print("  Caught: Division by zero")
    except ValueError:
        print("  Caught: Invalid value conversion")
    except IndexError:
        print("  Caught: Index out of range")

risky_operation("divide")
risky_operation("convert")
risky_operation("index")
print()

# 4. Catching multiple exceptions in one block
print("4. Catching multiple exceptions:")
try:
    # Could raise ValueError or TypeError
    data = {"key": [1, 2, 3]}
    value = int(data["key"])  # TypeError: can't convert list to int
except (ValueError, TypeError) as e:
    print(f"  Caught: {type(e).__name__} - {e}\n")

# 5. Generic exception (catch-all)
print("5. Generic exception (catch-all):")
try:
    unknown_operation = 5 + None  # TypeError
except Exception as e:
    print(f"  Caught generic exception: {type(e).__name__}: {e}\n")

# ============ COMMON EXCEPTIONS ============
print("=== COMMON EXCEPTIONS ===\n")

exceptions_info = [
    ("ValueError", "Converting invalid string to number"),
    ("TypeError", "Operating on wrong data types"),
    ("ZeroDivisionError", "Dividing by zero"),
    ("IndexError", "Accessing invalid list index"),
    ("KeyError", "Accessing non-existent dictionary key"),
    ("FileNotFoundError", "Opening non-existent file"),
    ("AttributeError", "Accessing non-existent attribute"),
    ("NameError", "Using undefined variable"),
    ("RuntimeError", "General runtime error"),
    ("ImportError", "Failed module import"),
]

print("Common exceptions and causes:")
for exc_name, cause in exceptions_info:
    print(f"  {exc_name}: {cause}")
print()

# ============ try-except-else ============
print("=== try-except-else ===\n")

print("The else clause runs only if NO exception occurred:\n")

# Example 1
try:
    num = int("42")  # Valid conversion
except ValueError:
    print("  Invalid number")
else:
    print(f"  Conversion successful: {num}")
print()

# Example 2: else with file operations
print("Example: Opening file with else clause:")
try:
    # Simulating file not found
    file_exists = False
    if not file_exists:
        raise FileNotFoundError("File not found")
except FileNotFoundError as e:
    print(f"  Error: {e}")
except Exception as e:
    print(f"  Unexpected error: {e}")
else:
    print("  File opened successfully")
    print("  Processing file...")
print()

# ============ try-except-finally ============
print("=== try-except-finally ===\n")

print("The finally clause ALWAYS runs (cleanup code):\n")

# Example 1: Cleanup with finally
def open_and_read():
    file = None
    try:
        print("  Opening file...")
        # file = open("data.txt")  # Simulate file operation
        raise FileNotFoundError("File not found")
    except FileNotFoundError as e:
        print(f"  Error: {e}")
    finally:
        print("  Cleanup: Closing resources...\n")

open_and_read()

# Example 2: Function return with finally
print("Example 2: finally runs even with return:\n")
def test_finally():
    try:
        print("  In try block")
        return "Returning from try"
    finally:
        print("  In finally block (always executes)")

result = test_finally()
print(f"  Result: {result}\n")

# Example 3: Exception handling complete flow
print("Example 3: Complete try-except-else-finally:\n")
def process_data(data):
    try:
        print(f"  Processing: {data}")
        result = int(data)
    except ValueError:
        print("  Error: Invalid data")
        result = None
    else:
        print(f"  Success: Converted to {result}")
        result = result * 2
    finally:
        print("  Cleanup complete\n")
    return result

process_data("25")
process_data("invalid")

# ============ RAISING EXCEPTIONS ============
print("=== RAISING EXCEPTIONS ===\n")

# 1. Basic raise
print("1. Basic raise:")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"  Caught: {e}\n")

# 2. Re-raising exceptions
print("2. Re-raising exceptions:")
def process_data_strict(data):
    try:
        num = int(data)
    except ValueError as e:
        print(f"  Original error: {e}")
        raise  # Re-raise the same exception

try:
    process_data_strict("abc")
except ValueError as e:
    print(f"  Caught in outer handler: {e}\n")

# 3. Raising different exception
print("3. Raising different exception:")
def read_file(filename):
    if not filename.endswith('.txt'):
        raise TypeError("File must be .txt")
    # Simulating file not found
    if filename == "nonexistent.txt":
        raise FileNotFoundError(f"File '{filename}' not found")

try:
    read_file("data")  # Wrong extension
except TypeError as e:
    print(f"  Caught: {type(e).__name__} - {e}\n")

# ============ CUSTOM EXCEPTIONS ============
print("=== CUSTOM EXCEPTIONS ===\n")

# Define custom exception
class InsufficientBalanceError(Exception):
    \"\"\"Raised when account balance is insufficient\"\"\"
    pass

class InvalidAmountError(Exception):
    \"\"\"Raised when amount is invalid\"\"\"
    pass

# Using custom exceptions
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient balance. Available: {self.balance}"
            )
        self.balance -= amount
        return self.balance

# Test custom exceptions
account = BankAccount(100)

try:
    account.withdraw(-10)  # Invalid amount
except InvalidAmountError as e:
    print(f"  Error: {e}")

try:
    account.withdraw(150)  # Insufficient balance
except InsufficientBalanceError as e:
    print(f"  Error: {e}")

try:
    account.withdraw(50)  # Valid
    print(f"  Withdrawal successful. New balance: {account.balance}\n")
except Exception as e:
    print(f"  Error: {e}\n")

# ============ EXCEPTION CONTEXT (CHAINING) ============
print("=== EXCEPTION CHAINING ===\n")

def read_config():
    try:
        with open("config.txt") as f:
            data = f.read()
            config = eval(data)  # Dangerous but for example
    except FileNotFoundError as e:
        # Chain exceptions
        raise RuntimeError("Configuration file not found") from e

try:
    read_config()
except RuntimeError as e:
    print(f"  High-level error: {e}")
    print(f"  Caused by: {e.__cause__}\n")

# ============ TRACEBACK ============
print("=== TRACEBACK ===\n")

def func_a():
    return func_b()

def func_b():
    return func_c()

def func_c():
    return 1 / 0

print("Full traceback:")
try:
    func_a()
except ZeroDivisionError:
    traceback.print_exc()
print()

# ============ ASSERTION ============
print("=== ASSERTION (Testing & Debugging) ===\n")

# Assertions are for testing assumptions during development
def divide(a, b):
    assert b != 0, "Divisor cannot be zero!"
    assert isinstance(a, (int, float)), "a must be number"
    assert isinstance(b, (int, float)), "b must be number"
    return a / b

print("Testing assertions:")
try:
    print(f"  divide(10, 2) = {divide(10, 2)}")
except AssertionError as e:
    print(f"  Assertion failed: {e}")

try:
    print(f"  divide(10, 0) = {divide(10, 0)}")
except AssertionError as e:
    print(f"  Assertion failed: {e}")

try:
    print(f"  divide('10', 2) = {divide('10', 2)}")
except AssertionError as e:
    print(f"  Assertion failed: {e}\n")

# ============ CONTEXT MANAGERS (with statement) ============
print("=== CONTEXT MANAGERS ===\n")

# Context managers ensure cleanup even if error occurs

print("1. File handling with context manager:")
print("  Without context manager (risky):")
print("""
    f = open("file.txt")
    data = f.read()
    f.close()  # May not run if error occurs!
    
  With context manager (safe):
    with open("file.txt") as f:
        data = f.read()  # File auto-closes
""")

# Example using StringIO (simulating file)
from io import StringIO

print("\n2. Using StringIO (file-like object):")
with StringIO("Hello\nWorld") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"  Line 1: {line1.strip()}")
    print(f"  Line 2: {line2.strip()}")
print()

# ============ PRACTICAL EXAMPLES ============
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Safe type conversion
print("Example 1: Safe type conversion:")
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"  safe_int('42') = {safe_int('42')}")
print(f"  safe_int('abc') = {safe_int('abc')}")
print(f"  safe_int('abc', -1) = {safe_int('abc', -1)}\n")

# Example 2: Input validation
print("Example 2: Input validation:")
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Must be positive")
            return value
        except ValueError as e:
            print(f"  Invalid input: {e}. Try again.")

# (Commented out because it requires user input)
"""
age = get_positive_integer("Enter your age: ")
print(f"You entered: {age}")
"""
print("  (Function commented out - requires user input)\n")

# Example 3: Retry logic
print("Example 3: Retry logic:")
import random

def unreliable_network_call(url):
    \"\"\"Simulates a network call that might fail\"\"\"
    if random.random() < 0.5:
        raise ConnectionError("Network unreliable")
    return f"Data from {url}"

def call_with_retry(url, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            return unreliable_network_call(url)
        except ConnectionError as e:
            if attempt < max_retries:
                print(f"  Attempt {attempt} failed. Retrying...")
            else:
                print(f"  All {max_retries} attempts failed")
                raise

try:
    result = call_with_retry("example.com", max_retries=2)
    print(f"  Success: {result}\n")
except ConnectionError:
    print("  Final failure\n")

# ============ BEST PRACTICES ============
print("=== BEST PRACTICES FOR EXCEPTION HANDLING ===\n")
print("""
1. BE SPECIFIC:
   ❌ except:
   ✓ except ValueError:

2. HANDLE AT APPROPRIATE LEVEL:
   - Handle where you can fix the problem
   - Let other exceptions propagate

3. USE FINALLY FOR CLEANUP:
   - Close files
   - Release database connections
   - Free resources

4. PROVIDE MEANINGFUL MESSAGES:
   raise ValueError(f"Age {age} is invalid (expected 0-150)")

5. LOG EXCEPTIONS:
   import logging
   logging.exception("An error occurred")

6. DON'T IGNORE EXCEPTIONS:
   ❌ except: pass
   ✓ except SomeError as e:
       print(f"Error: {e}")
       handle_error(e)

7. USE CONTEXT MANAGERS:
   ✓ with open("file.txt") as f:
       data = f.read()

8. VALIDATE INPUT EARLY:
   - Check types
   - Check ranges
   - Fail fast

9. USE ASSERTIONS FOR DEVELOPMENT:
   assert x > 0, "x must be positive"

10. CLEAN UP RESOURCES:
    try:
        use_resource()
    finally:
        cleanup_resource()
""")
