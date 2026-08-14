"""
isalnum_example.py

Explain and demonstrate str.isalnum().
"""

EXPLANATION = """
s.isalnum() returns True if the string is non-empty and all characters
are alphanumeric (letters or digits). It returns False for strings with
spaces or punctuation.
"""


def demonstrate():
    samples = ["abc123", "abc 123", "", "123", "abc!"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.isalnum()}')


if __name__ == '__main__':
    demonstrate()
