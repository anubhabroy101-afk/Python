"""
==============================================================
CHAPTER 8: MODULES & LIBRARIES
==============================================================
Using built-in tools

- Importing modules
- pip installer
- math, random, statistics modules

==============================================================
"""

import sys
import os

# ============ IMPORTING MODULES ============
print("=== IMPORTING MODULES ===\n")

# 1. Import entire module
import math

print("1. Importing entire module (import math):")
print(f"   math.pi = {math.pi}")
print(f"   math.sqrt(16) = {math.sqrt(16)}")
print(f"   math.ceil(3.2) = {math.ceil(3.2)}")
print(f"   math.floor(3.9) = {math.floor(3.9)}\n")

# 2. Import specific functions
from math import sqrt, pi, factorial

print("2. Importing specific functions (from math import sqrt, pi, factorial):")
print(f"   sqrt(25) = {sqrt(25)}")
print(f"   pi = {pi}")
print(f"   factorial(5) = {factorial(5)}\n")

# 3. Import with alias
from math import sqrt as square_root

print("3. Importing with alias (from math import sqrt as square_root):")
print(f"   square_root(36) = {square_root(36)}\n")

# 4. Import all (use carefully!)
# from math import *  # Not recommended

print("4. Import all: 'from math import *' (not recommended)")
print("   Imports all public names from module\n")

# ============ MATH MODULE ============
print("=== MATH MODULE ===\n")

import math

print("1. Constants:")
print(f"   math.pi = {math.pi}")
print(f"   math.e = {math.e}")
print(f"   math.tau = {math.tau}\n")

print("2. Basic functions:")
print(f"   math.fabs(-5) = {math.fabs(-5)}")
print(f"   math.sqrt(16) = {math.sqrt(16)}")
print(f"   math.pow(2, 3) = {math.pow(2, 3)}\n")

print("3. Rounding functions:")
print(f"   math.ceil(3.2) = {math.ceil(3.2)}")
print(f"   math.floor(3.9) = {math.floor(3.9)}")
print(f"   math.trunc(3.7) = {math.trunc(3.7)}\n")

print("4. Trigonometric functions (in radians):")
angle = math.pi / 4  # 45 degrees
print(f"   angle = π/4 radians (45 degrees)")
print(f"   math.sin(angle) = {math.sin(angle):.4f}")
print(f"   math.cos(angle) = {math.cos(angle):.4f}")
print(f"   math.tan(angle) = {math.tan(angle):.4f}\n")

print("5. Logarithmic functions:")
print(f"   math.log(10) = {math.log(10):.4f}")  # Natural log
print(f"   math.log10(100) = {math.log10(100)}")
print(f"   math.log2(8) = {math.log2(8)}\n")

print("6. Factorial and combinations:")
print(f"   math.factorial(5) = {math.factorial(5)}")
print(f"   math.gcd(48, 18) = {math.gcd(48, 18)}")  # Greatest common divisor
print()

# ============ RANDOM MODULE ============
print("=== RANDOM MODULE ===\n")

import random

print("1. Random float [0, 1):")
for _ in range(3):
    print(f"   random.random() = {random.random():.4f}")
print()

print("2. Random integer in range:")
print(f"   random.randint(1, 10) = {random.randint(1, 10)}")
print(f"   random.randint(1, 10) = {random.randint(1, 10)}\n")

print("3. Random choice from sequence:")
colors = ['red', 'blue', 'green', 'yellow']
print(f"   Colors: {colors}")
print(f"   random.choice(colors) = '{random.choice(colors)}'")
print(f"   random.choice(colors) = '{random.choice(colors)}'\n")

print("4. Random sample (no replacement):")
numbers = list(range(1, 11))
print(f"   Numbers: {numbers}")
sample = random.sample(numbers, 3)
print(f"   random.sample(numbers, 3) = {sample}\n")

print("5. Shuffle list:")
deck = ['A', 'K', 'Q', 'J', '10']
print(f"   Original: {deck}")
random.shuffle(deck)
print(f"   After shuffle: {deck}\n")

print("6. Random float in range:")
print(f"   random.uniform(1, 10) = {random.uniform(1, 10):.2f}\n")

# ============ STATISTICS MODULE ============
print("=== STATISTICS MODULE ===\n")

from statistics import mean, median, mode, stdev, variance

data = [2, 4, 4, 4, 5, 5, 7, 9]

print(f"Data: {data}\n")
print(f"mean() = {mean(data)}")
print(f"median() = {median(data)}")
print(f"mode() = {mode(data)}")
print(f"stdev() = {stdev(data):.4f}")  # Standard deviation
print(f"variance() = {variance(data):.4f}\n")

# ============ STRING MODULE ============
print("=== STRING MODULE ===\n")

import string

print(f"string.ascii_letters = {string.ascii_letters}")
print(f"string.ascii_lowercase = {string.ascii_lowercase}")
print(f"string.ascii_uppercase = {string.ascii_uppercase}")
print(f"string.digits = {string.digits}")
print(f"string.punctuation = {string.punctuation}\n")

# ============ DATETIME MODULE ============
print("=== DATETIME MODULE ===\n")

from datetime import datetime, date, timedelta

print("1. Current date and time:")
now = datetime.now()
print(f"   Current datetime: {now}")
print(f"   Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"   Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}\n")

print("2. Current date:")
today = date.today()
print(f"   Today: {today}\n")

print("3. Creating specific date:")
specific_date = date(2024, 12, 25)
print(f"   Specific date: {specific_date}\n")

print("4. Date arithmetic:")
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"   Today: {today}")
print(f"   Tomorrow: {tomorrow}")
print(f"   Next week: {next_week}\n")

# ============ OS MODULE ============
print("=== OS MODULE ===\n")

print("1. Current working directory:")
print(f"   os.getcwd() = {os.getcwd()}\n")

print("2. List files in current directory:")
files = os.listdir('.')
print(f"   os.listdir('.'): (showing first 5)")
for file in files[:5]:
    print(f"     {file}")
print()

print("3. Check if path exists:")
print(f"   os.path.exists('.') = {os.path.exists('.')}")
print(f"   os.path.exists('nonexistent.txt') = {os.path.exists('nonexistent.txt')}\n")

print("4. Check if is file or directory:")
print(f"   os.path.isfile('README.md') = {os.path.isfile('README.md')}")
print(f"   os.path.isdir('.') = {os.path.isdir('.')}\n")

# ============ COLLECTIONS MODULE ============
print("=== COLLECTIONS MODULE ===\n")

from collections import Counter, defaultdict, deque

print("1. Counter (count occurrences):")
text = "hello world"
char_count = Counter(text)
print(f"   Text: '{text}'")
print(f"   Counter(text) = {char_count}")
print(f"   Most common 3: {char_count.most_common(3)}\n")

print("2. defaultdict (default values for missing keys):")
dd = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    dd[word] += 1
print(f"   Words: {words}")
print(f"   Count: {dict(dd)}\n")

print("3. deque (double-ended queue):")
d = deque([1, 2, 3])
print(f"   Initial: {d}")
d.append(4)
print(f"   After append(4): {d}")
d.appendleft(0)
print(f"   After appendleft(0): {d}")
d.pop()
print(f"   After pop(): {d}")
d.popleft()
print(f"   After popleft(): {d}\n")

# ============ ITERTOOLS MODULE ============
print("=== ITERTOOLS MODULE ===\n")

from itertools import permutations, combinations, product

print("1. Permutations (order matters):")
items = ['A', 'B', 'C']
print(f"   Items: {items}")
print(f"   Permutations of 2 items:")
for perm in permutations(items, 2):
    print(f"     {perm}")
print()

print("2. Combinations (order doesn't matter):")
print(f"   Combinations of 2 items:")
for combo in combinations(items, 2):
    print(f"     {combo}")
print()

print("3. Cartesian product:")
colors = ['Red', 'Blue']
sizes = ['S', 'M']
print(f"   Colors: {colors}, Sizes: {sizes}")
for combo in product(colors, sizes):
    print(f"     {combo}")
print()

# ============ INSTALLING PACKAGES WITH PIP ============
print("=== PIP (PACKAGE INSTALLER) ===\n")
print("""
PIP is Python's package manager for installing external packages.

Installation:
  pip install package_name
  pip install package_name==1.0.0  (specific version)
  pip install package_name>=1.0.0

Uninstall:
  pip uninstall package_name

List installed:
  pip list

Search:
  pip search keyword

Common packages:
  - requests: HTTP library
  - numpy: Numerical computing
  - pandas: Data analysis
  - flask: Web framework
  - django: Web framework
  - beautifulsoup4: Web scraping
  - matplotlib: Data visualization
  - pygame: Game development
  - scikit-learn: Machine learning
""")

# ============ MODULE INFORMATION ============
print("=== MODULE INFORMATION ===\n")

print("Available functions in math module:")
math_functions = [name for name in dir(math) if not name.startswith('_')]
print(f"Total: {len(math_functions)}")
print(f"First 10: {math_functions[:10]}\n")

# ============ CREATING YOUR OWN MODULE ============
print("=== CREATING YOUR OWN MODULE ===\n")
print("""
To create a module:
1. Create a .py file with functions/classes
2. Import it in other files using: import filename

Example:
File: utils.py
-------
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

File: main.py
-------
import utils
print(utils.greet("Alice"))
print(utils.add(5, 3))

Output:
-------
Hello, Alice!
8
""")

# ============ PRACTICAL EXAMPLE ============
print("=== PRACTICAL EXAMPLE: GAME DICE SIMULATOR ===\n")

import random

def roll_dice(sides=6, num_dice=1):
    """Roll dice and return total"""
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return rolls, sum(rolls)

# Simulate rolling 2 six-sided dice 5 times
print("Rolling 2 six-sided dice 5 times:")
for game in range(1, 6):
    rolls, total = roll_dice(num_dice=2)
    print(f"  Game {game}: {rolls} = {total}")
print()

# Probability experiment
print("Probability experiment: Roll 1 die 1000 times")
rolls = [random.randint(1, 6) for _ in range(1000)]
from collections import Counter
distribution = Counter(rolls)
print(f"  Distribution: {sorted(distribution.items())}")
print(f"  Mean: {sum(rolls) / len(rolls):.2f}")
