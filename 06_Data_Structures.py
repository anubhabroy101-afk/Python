"""
==============================================================
CHAPTER 6: DATA STRUCTURES (CORE DATA HANDLING)
==============================================================
Very important — high exam + practical weight

A. Strings
- String basics
- Indexing & slicing
- Traversal
- String operations & functions

B. Lists
- Creating lists
- Indexing, slicing
- Nested lists
- Shallow vs deep copy
- List methods

C. Tuples
- Tuple basics
- Packing & unpacking
- Tuple operations

D. Dictionaries
- Key-value structure
- Accessing & updating
- Nested dictionaries
- Dictionary methods

==============================================================
"""

import copy

# ============ STRINGS ============
print("=== STRINGS ===\n")

# 1. String basics
print("1. String basics:")
text = "Python Programming"
print(f"  Text: {text}")
print(f"  Length: {len(text)}")
print(f"  Type: {type(text)}\n")

# 2. String indexing
print("2. String indexing:")
print(f"  First character: {text[0]}")
print(f"  Last character: {text[-1]}")
print(f"  Character at index 7: {text[7]}\n")

# 3. String slicing
print("3. String slicing:")
print(f"  text[0:6]: {text[0:6]}")  # 'Python'
print(f"  text[7:]: {text[7:]}")  # 'Programming'
print(f"  text[:6]: {text[:6]}")  # 'Python'
print(f"  text[::2]: {text[::2]}")  # Every 2nd character
print(f"  text[::-1]: {text[::-1]}\n")  # Reversed

# 4. String traversal
print("4. String traversal:")
print("  Characters in 'Python':")
for char in "Python":
    print(f"    {char}")
print()

# 5. String immutability
print("5. String immutability:")
original = "Hello"
print(f"  Original: {original}")
# original[0] = "J"  # Error! Strings are immutable
modified = "J" + original[1:]  # Create new string
print(f"  Modified: {modified}\n")

# 6. String operations
print("6. String operations:")
s1 = "Hello"
s2 = "World"
print(f"  Concatenation: {s1} + {s2} = {s1 + ' ' + s2}")
print(f"  Repetition: 'Hi' * 3 = {'Hi' * 3}")
print(f"  Membership: 'o' in 'Hello': {'o' in 'Hello'}\n")

# 7. String methods
print("7. String methods:")
text = "  Python Programming  "
print(f"  Original: '{text}'")
print(f"  strip(): '{text.strip()}'")
print(f"  upper(): '{text.upper()}'")
print(f"  lower(): '{text.lower()}'")
print(f"  replace(): '{text.replace('Python', 'Java')}'")
print(f"  split(): {text.split()}")
print(f"  startswith('  Py'): {text.startswith('  Py')}")
print(f"  count('P'): {text.count('P')}\n")

# ============ LISTS ============
print("=== LISTS ===\n")

# 1. Creating lists
print("1. Creating lists:")
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
mixed_list = [1, 'hello', 3.14, True]
print(f"  list1: {list1}")
print(f"  list2: {list2}")
print(f"  mixed_list: {mixed_list}\n")

# 2. List indexing
print("2. List indexing:")
nums = [10, 20, 30, 40, 50]
print(f"  nums: {nums}")
print(f"  nums[0]: {nums[0]}")
print(f"  nums[-1]: {nums[-1]}")
print(f"  nums[2]: {nums[2]}\n")

# 3. List slicing
print("3. List slicing:")
print(f"  nums[1:4]: {nums[1:4]}")
print(f"  nums[:3]: {nums[:3]}")
print(f"  nums[2:]: {nums[2:]}")
print(f"  nums[::2]: {nums[::2]}")
print(f"  nums[::-1]: {nums[::-1]}\n")

# 4. List modification
print("4. List modification:")
numbers = [1, 2, 3, 4, 5]
print(f"  Original: {numbers}")
numbers[0] = 10
print(f"  After numbers[0] = 10: {numbers}")
numbers[1:3] = [20, 30, 40]
print(f"  After numbers[1:3] = [20, 30, 40]: {numbers}\n")

# 5. List methods
print("5. List methods:")
items = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"  items: {items}")

items_copy = items.copy()
items_copy.append(7)
print(f"  append(7): {items_copy}")

items_copy2 = items.copy()
items_copy2.insert(0, 0)
print(f"  insert(0, 0): {items_copy2}")

items_copy3 = items.copy()
items_copy3.remove(1)  # Removes first occurrence
print(f"  remove(1): {items_copy3}")

items_copy4 = items.copy()
popped = items_copy4.pop()
print(f"  pop(): removed {popped}, list: {items_copy4}")

items_copy5 = items.copy()
items_copy5.sort()
print(f"  sort(): {items_copy5}")

items_copy6 = items.copy()
items_copy6.reverse()
print(f"  reverse(): {items_copy6}")

items_copy7 = items.copy()
print(f"  index(5): {items_copy7.index(5)}")
print(f"  count(1): {items_copy7.count(1)}\n")

# 6. List iteration
print("6. List iteration:")
fruits = ['apple', 'banana', 'cherry']
print("  Using for loop:")
for fruit in fruits:
    print(f"    {fruit}")
print()

# 7. List comprehension
print("7. List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"  Squares 1-5: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"  Even numbers 0-9: {evens}\n")

# 8. Nested lists
print("8. Nested lists:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"  matrix: {matrix}")
print(f"  matrix[0]: {matrix[0]}")
print(f"  matrix[1][2]: {matrix[1][2]}")
print()

# 9. Shallow vs Deep copy
print("9. Shallow vs Deep copy:")
original_nested = [[1, 2], [3, 4]]
shallow = original_nested.copy()
deep = copy.deepcopy(original_nested)

print(f"  Original: {original_nested}")
print(f"  Shallow copy: {shallow}")
print(f"  Deep copy: {deep}")

# Modify original
original_nested[0][0] = 99
print(f"\n  After original[0][0] = 99:")
print(f"  Original: {original_nested}")
print(f"  Shallow (affected): {shallow}")
print(f"  Deep (not affected): {deep}\n")

# ============ TUPLES ============
print("=== TUPLES ===\n")

# 1. Creating tuples
print("1. Creating tuples:")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
single_element = (1,)  # Comma needed for single element
mixed_tuple = (1, 'hello', 3.14)

print(f"  tuple1: {tuple1}")
print(f"  tuple2: {tuple2}")
print(f"  single_element: {single_element}")
print(f"  mixed_tuple: {mixed_tuple}\n")

# 2. Tuple indexing and slicing
print("2. Tuple indexing and slicing:")
coords = (10, 20, 30)
print(f"  coords: {coords}")
print(f"  coords[0]: {coords[0]}")
print(f"  coords[1:]: {coords[1:]}\n")

# 3. Tuple immutability
print("3. Tuple immutability:")
# coords[0] = 100  # Error! Tuples are immutable
print("  Tuples cannot be modified (immutable)\n")

# 4. Tuple packing
print("4. Tuple packing (creating from values):")
values = 1, 2, 3
print(f"  values = 1, 2, 3: {values}\n")

# 5. Tuple unpacking
print("5. Tuple unpacking (extracting values):")
a, b, c = (10, 20, 30)
print(f"  a, b, c = (10, 20, 30)")
print(f"  a={a}, b={b}, c={c}")

x, y, *rest = (1, 2, 3, 4, 5)
print(f"  x, y, *rest = (1, 2, 3, 4, 5)")
print(f"  x={x}, y={y}, rest={rest}\n")

# 6. Tuple methods
print("6. Tuple methods:")
items_tuple = (1, 2, 3, 2, 4, 2)
print(f"  items_tuple: {items_tuple}")
print(f"  count(2): {items_tuple.count(2)}")
print(f"  index(3): {items_tuple.index(3)}\n")

# 7. Tuple unpacking in loops
print("7. Tuple unpacking in loops:")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(f"  {num}: {letter}")
print()

# ============ DICTIONARIES ============
print("=== DICTIONARIES ===\n")

# 1. Creating dictionaries
print("1. Creating dictionaries:")
person = {"name": "Alice", "age": 25, "city": "NYC"}
scores = {"math": 90, "english": 85, "science": 92}
empty_dict = {}

print(f"  person: {person}")
print(f"  scores: {scores}\n")

# 2. Accessing values
print("2. Accessing values:")
print(f"  person['name']: {person['name']}")
print(f"  person.get('age'): {person.get('age')}")
print(f"  person.get('country', 'USA'): {person.get('country', 'USA')}\n")

# 3. Modifying dictionaries
print("3. Modifying dictionaries:")
person['age'] = 26
person['country'] = 'USA'
print(f"  After modifications: {person}\n")

# 4. Removing items
print("4. Removing items:")
data = {"a": 1, "b": 2, "c": 3}
print(f"  Original: {data}")
del data["b"]
print(f"  After del data['b']: {data}\n")

# 5. Dictionary methods
print("5. Dictionary methods:")
student = {"name": "Bob", "roll": 101, "grade": "A"}
print(f"  student: {student}")
print(f"  keys(): {student.keys()}")
print(f"  values(): {student.values()}")
print(f"  items(): {student.items()}")
print(f"  len(): {len(student)}\n")

# 6. Dictionary iteration
print("6. Dictionary iteration:")
print("  Iterating over keys:")
for key in student:
    print(f"    {key}: {student[key]}")

print("  Iterating with items():")
for key, value in student.items():
    print(f"    {key}: {value}\n")

# 7. Nested dictionaries
print("7. Nested dictionaries:")
company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "Alice", "salary": 50000},
        "emp2": {"name": "Bob", "salary": 60000}
    }
}
print(f"  company['name']: {company['name']}")
print(f"  emp1 name: {company['employees']['emp1']['name']}")
print(f"  emp2 salary: {company['employees']['emp2']['salary']}\n")

# 8. Dictionary comprehension
print("8. Dictionary comprehension:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"  {squares_dict}\n")

# ============ COMPARISON OF DATA STRUCTURES ============
print("=== COMPARISON OF DATA STRUCTURES ===\n")
print("""
STRINGS:
- Immutable (cannot be changed)
- Ordered (index-based)
- Support indexing and slicing
- Methods: upper(), lower(), split(), etc.

LISTS:
- Mutable (can be modified)
- Ordered (index-based)
- Can contain mixed types
- Support indexing, slicing, sorting
- Methods: append(), remove(), sort(), etc.

TUPLES:
- Immutable (cannot be changed)
- Ordered (index-based)
- Faster than lists
- Used as dictionary keys
- Can be unpacked easily

DICTIONARIES:
- Mutable (can be modified)
- Unordered (key-based, not indexed)
- Keys must be unique and immutable
- Fast lookup by key
- Methods: keys(), values(), items(), etc.
""")
