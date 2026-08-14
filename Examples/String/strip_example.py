"""
strip_example.py

Explain and demonstrate str.strip([chars]).
"""

EXPLANATION = """
s.strip(chars) returns a copy of the string with leading and trailing
characters removed. If chars is None (default), whitespace is removed.
chars is interpreted as a set of characters, not a substring.
"""


def demonstrate():
    s = '   hello  '
    s2 = '***example***'
    print(EXPLANATION)
    print('s ->', repr(s))
    print('s.strip() ->', repr(s.strip()))
    print('s2.strip("*") ->', repr(s2.strip('*')))


if __name__ == '__main__':
    demonstrate()
