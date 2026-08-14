"""
string_methods.py

A compact reference and runnable examples for common Python string functions and methods.

Includes: len, capitalize, title, swapcase, isalnum, isalpha, isdigit, isspace,
islower, isupper, find, index, lower, upper, replace, join, split, partition,
count, startswith, lstrip, rstrip, strip, removeprefix, removesuffix

Run the module as a script to see output examples.
"""

EXAMPLES_DOC = """
Examples shown by this module (short):
- len(s)
- s.capitalize(), s.title(), s.swapcase()
- s.isalnum(), s.isalpha(), s.isdigit(), s.isspace(), s.islower(), s.isupper()
- s.find(sub), s.index(sub)
- s.lower(), s.upper(), s.replace(old, new, count)
- sep.join(iterable), s.split(sep, maxsplit)
- s.partition(sep) -> (before, sep, after)
- s.count(sub)
- s.startswith(prefix), s.endswith(suffix)
- s.lstrip(chars), s.rstrip(chars), s.strip(chars)
- s.removeprefix(prefix), s.removesuffix(suffix)  # Python 3.9+
"""


def demonstrate():
    s = "  Hello, World!  "
    alpha = "Python"
    numeric = "2026"
    mixed = "Py3"

    print('\n--- Basic measurements and case ---')
    print('Original repr:', repr(s))
    print('len(s):', len(s))
    print('s.strip():', repr(s.strip()))  # removes surrounding whitespace
    print('s.capitalize():', s.strip().capitalize())  # "Hello, world!"
    print('s.title():', s.strip().title())  # Each word capitalized
    print('s.swapcase():', s.strip().swapcase())  # Invert case

    print('\n--- Character-type checks ---')
    print("alpha.isalpha() ->", alpha.isalpha())
    print("numeric.isdigit() ->", numeric.isdigit())
    print("mixed.isalnum() ->", mixed.isalnum())
    print("'   '.isspace() ->", '   '.isspace())
    print("'abc'.islower() ->", 'abc'.islower())
    print("'ABC'.isupper() ->", 'ABC'.isupper())

    print('\n--- Searching and indexing ---')
    print("s.find('o') ->", s.find('o'))  # returns -1 if not found
    try:
        print("s.index('o') ->", s.index('o'))  # raises ValueError if not found
    except ValueError as e:
        print('index raised:', e)

    print("s.count('l') ->", s.count('l'))

    print('\n--- Case conversion and replace ---')
    print("s.lower() ->", s.lower())
    print("s.upper() ->", s.upper())
    print("s.replace('l', 'L', 1) ->", s.replace('l', 'L', 1))  # only first occurrence

    print('\n--- Splitting, joining, partition ---')
    csv = 'one,two,three'
    parts = csv.split(',')
    print('csv.split(",") ->', parts)
    print("'-'.join(parts) ->", '-'.join(parts))

    text = 'user@example.com'
    before, sep, after = text.partition('@')
    print("text.partition('@') ->", (before, sep, after))

    print('\n--- startswith / endswith ---')
    print("text.startswith('user') ->", text.startswith('user'))
    print("text.endswith('.com') ->", text.endswith('.com'))

    print('\n--- Strip variants ---')
    messy = '---example---'
    print("messy.lstrip('-') ->", messy.lstrip('-'))
    print("messy.rstrip('-') ->", messy.rstrip('-'))
    print("messy.strip('-') ->", messy.strip('-'))

    print('\n--- removeprefix / removesuffix (3.9+) ---')
    s2 = 'pre_fix_example_suffix'
    print('s2:', s2)
    print("s2.removeprefix('pre_') ->", s2.removeprefix('pre_'))
    print("s2.removesuffix('_suffix') ->", s2.removesuffix('_suffix'))

    print('\n--- Notes / differences ---')
    print('find vs index: find returns -1 if not found; index raises ValueError')
    print('join expects an iterable of strings; it is called on the separator')
    print('split without argument splits on any whitespace and strips edge whitespace')


if __name__ == '__main__':
    print('String methods reference and demonstration')
    print(EXAMPLES_DOC)
    demonstrate()
