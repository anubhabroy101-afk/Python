"""
==============================================================
CHAPTER 7: FUNCTIONS & MODULARITY
==============================================================
Code reuse and structure

- Defining & calling functions
- Arguments & return types
- Scope & namespace
- Mutable vs immutable arguments
- Recursion
- Lambda functions

==============================================================
"""

# ============ DEFINING & CALLING FUNCTIONS ============
print("=== DEFINING & CALLING FUNCTIONS ===\n")

# 1. Simple function
def greet():
    print("Hello, World!")

greet()
print()

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
print()

# 3. Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}\n")

# 4. Function with multiple return values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(f"Coordinates: x={x}, y={y}\n")

# ============ PARAMETERS & ARGUMENTS ============
print("=== PARAMETERS & ARGUMENTS ===\n")

# 1. Positional arguments
def multiply(a, b):
    return a * b

print(f"multiply(3, 4) = {multiply(3, 4)}\n")

# 2. Keyword arguments
def describe_person(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

describe_person("Alice", 25)
describe_person("Bob", 30, "NYC")
describe_person("Eve", city="LA", age=28)
print()

# 3. Default arguments
def power(base, exponent=2):
    return base ** exponent

print(f"power(5) = {power(5)}")  # 5^2
print(f"power(5, 3) = {power(5, 3)}")  # 5^3
print()

# 4. Variable-length arguments (*args)
def sum_numbers(*args):
    print(f"Received arguments: {args}")
    return sum(args)

print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(10, 20, 30, 40) = {sum_numbers(10, 20, 30, 40)}\n")

# 5. Keyword variable-length arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("print_info with keyword arguments:")
print_info(name="Alice", age=25, city="NYC")
print()

# 6. Combining *args and **kwargs
def flexible_function(a, b, *args, **kwargs):
    print(f"Required args: a={a}, b={b}")
    print(f"Extra args: {args}")
    print(f"Extra kwargs: {kwargs}\n")

flexible_function(1, 2, 3, 4, 5, name="Alice", age=25)

# ============ FUNCTION DOCUMENTATION ============
print("=== FUNCTION DOCUMENTATION ===\n")

def calculate_area(length, width):
    \"""
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        float: Area of rectangle
    \"""
    return length * width

print("Function docstring:")
print(calculate_area.__doc__)
print(f"Area of 5x4 rectangle: {calculate_area(5, 4)}\n")

# ============ SCOPE & NAMESPACE ============
print("=== SCOPE & NAMESPACE ===\n")

x = 100  # Global variable

def scope_example():
    x = 50  # Local variable (shadows global)
    print(f"Inside function: x = {x}")
    y = 75  # Local variable
    print(f"Inside function: y = {y}")

print(f"Before function: x = {x}")
scope_example()
print(f"After function: x = {x}")
# print(y)  # Error! y only exists inside function
print()

# Modifying global variable
global_counter = 0

def increment():
    global global_counter  # Access global variable
    global_counter += 1

print(f"Counter: {global_counter}")
increment()
print(f"After increment: {global_counter}")
increment()
print(f"After increment: {global_counter}\n")

# ============ MUTABLE VS IMMUTABLE ARGUMENTS ============
print("=== MUTABLE VS IMMUTABLE ARGUMENTS ===\n")

# 1. Immutable arguments (int, string, tuple)
def modify_immutable(num):
    num = num + 10  # Creates new object
    return num

original_num = 5
print(f"Original: {original_num}")
result = modify_immutable(original_num)
print(f"After function: {original_num} (unchanged)")
print(f"Returned: {result}\n")

# 2. Mutable arguments (list, dict)
def modify_mutable(lst):
    lst.append(99)  # Modifies original object

numbers = [1, 2, 3]
print(f"Before function: {numbers}")
modify_mutable(numbers)
print(f"After function: {numbers} (changed!)\n")

# Avoiding unwanted modifications
def safe_modify(lst):
    new_list = lst.copy()  # Make a copy first
    new_list.append(99)
    return new_list

original_list = [1, 2, 3]
print(f"Before safe function: {original_list}")
modified = safe_modify(original_list)
print(f"After safe function: {original_list} (unchanged)")
print(f"Returned: {modified}\n")

# ============ RECURSION ============
print("=== RECURSION ===\n")

# 1. Simple recursion - Factorial
def factorial(n):
    if n <= 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

print("Factorial:")
for i in range(1, 6):
    print(f"  {i}! = {factorial(i)}")
print()

# 2. Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 10 numbers):")
fib_numbers = [fibonacci(i) for i in range(10)]
print(f"  {fib_numbers}\n")

# 3. Sum of list elements
def sum_list(lst):
    if len(lst) == 0:  # Base case
        return 0
    else:  # Recursive case
        return lst[0] + sum_list(lst[1:])

test_list = [1, 2, 3, 4, 5]
print(f"Sum of {test_list} = {sum_list(test_list)}\n")

# 4. Tree traversal example
def print_tree(items, level=0):
    for item in items:
        if isinstance(item, list):
            print_tree(item, level + 1)
        else:
            print("  " * level + str(item))

print("Tree structure:")
tree = [1, [2, 3], [4, [5, 6]]]
print_tree(tree)
print()

# ============ LAMBDA FUNCTIONS ============
print("=== LAMBDA FUNCTIONS ===\n")

# 1. Simple lambda
square = lambda x: x ** 2
print(f"Lambda: square = lambda x: x ** 2")
print(f"square(5) = {square(5)}\n")

# 2. Lambda with multiple arguments
add_lambda = lambda x, y: x + y
print(f"Lambda: add = lambda x, y: x + y")
print(f"add_lambda(3, 4) = {add_lambda(3, 4)}\n")

# 3. Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"map(lambda x: x*2, {numbers}):")
print(f"  {doubled}\n")

# 4. Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x%2==0, {numbers}):")
print(f"  {evens}\n")

# 5. Lambda with sorted()
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"Sorted by score:")
for name, score in sorted_by_score:
    print(f"  {name}: {score}")
print()

# ============ HIGHER-ORDER FUNCTIONS ============
print("=== HIGHER-ORDER FUNCTIONS ===\n")

# Function that takes another function as argument
def apply_operation(a, b, operation):
    return operation(a, b)

add_op = lambda x, y: x + y
multiply_op = lambda x, y: x * y

print(f"apply_operation(5, 3, add_op) = {apply_operation(5, 3, add_op)}")
print(f"apply_operation(5, 3, multiply_op) = {apply_operation(5, 3, multiply_op)}\n")

# Function that returns another function
def make_multiplier(factor):
    return lambda x: x * factor

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(f"times_three = make_multiplier(3)")
print(f"times_three(10) = {times_three(10)}")
print(f"times_five(10) = {times_five(10)}\n")

# ============ DECORATORS (INTRODUCTION) ============
print("=== DECORATORS (INTRODUCTION) ===\n")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  Returned: {result}")
        return result
    return wrapper

@my_decorator
def add_decorated(a, b):
    return a + b

print("With decorator:")
result = add_decorated(3, 4)
print()

# ============ PRACTICE FUNCTIONS ============
print("=== PRACTICE FUNCTIONS ===\n")

# 1. Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers 1-20:")
primes = [n for n in range(1, 21) if is_prime(n)]
print(f"  {primes}\n")

# 2. Reverse string
def reverse_string(s):
    return s[::-1]

print(f"reverse_string('Python') = '{reverse_string('Python')}'\n")

# 3. Count vowels
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

print(f"count_vowels('Python Programming') = {count_vowels('Python Programming')}\n")

# 4. Find maximum in list
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

print(f"find_max([3, 1, 4, 1, 5, 9]) = {find_max([3, 1, 4, 1, 5, 9])}\n")

# 5. Remove duplicates
def remove_duplicates(lst):
    return list(set(lst))

print(f"remove_duplicates([1, 2, 2, 3, 3, 3]) = {remove_duplicates([1, 2, 2, 3, 3, 3])}")
