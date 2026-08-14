"""
lstrip_example.py

Explain and demonstrate str.lstrip([chars]).
"""

EXPLANATION = """
s.lstrip(chars) returns a copy of the string with leading characters
removed. If chars is None (default), whitespace is removed. chars is
a set of characters, not a prefix string.
"""


def demonstrate():
    s = '   hello  '
    s2 = '---hello---'
    print(EXPLANATION)
    print('s ->', repr(s))
    print('s.lstrip() ->', repr(s.lstrip()))
    print('s2.lstrip("-") ->', repr(s2.lstrip('-')))


if __name__ == '__main__':
    demonstrate()
