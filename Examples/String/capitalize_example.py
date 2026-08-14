"""
capitalize_example.py

Explain and demonstrate str.capitalize().
"""

EXPLANATION = """
s.capitalize() returns a copy of the string with its first character
converted to uppercase and the rest to lowercase.
Useful for normalizing single-word inputs.
"""


def demonstrate():
    samples = ["hello", "hELLo", "123abc", ""]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {repr(s.capitalize())}')


if __name__ == '__main__':
    demonstrate()
