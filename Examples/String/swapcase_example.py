"""
swapcase_example.py

Explain and demonstrate str.swapcase().
"""

EXPLANATION = """
s.swapcase() returns a copy of the string with uppercase characters
converted to lowercase and vice versa. Useful for toggling case for
visual demonstration or ad-hoc normalization checks.
"""


def demonstrate():
    samples = ["Hello World", "mIxEd123", "LOWER", "UPPER"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {repr(s.swapcase())}')


if __name__ == '__main__':
    demonstrate()
