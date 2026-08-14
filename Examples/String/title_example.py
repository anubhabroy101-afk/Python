"""
title_example.py

Explain and demonstrate str.title().
"""

EXPLANATION = """
s.title() returns a title-cased version of the string: first letter of
each word is uppercased and the remaining letters are lowercased.
It treats non-letter characters as word boundaries.
"""


def demonstrate():
    samples = ["this is a test", "ANOTHER-test", "o'reilly"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {repr(s.title())}')


if __name__ == '__main__':
    demonstrate()
