"""
rstrip_example.py

Explain and demonstrate str.rstrip([chars]).
"""

EXPLANATION = """
s.rstrip(chars) returns a copy of the string with trailing characters
removed. If chars is None (default), whitespace is removed. chars is a
set of characters, not a suffix string.
"""


def demonstrate():
    s = '   hello  '
    s2 = '---hello---'
    print(EXPLANATION)
    print('s ->', repr(s))
    print('s.rstrip() ->', repr(s.rstrip()))
    print('s2.rstrip("-") ->', repr(s2.rstrip('-')))


if __name__ == '__main__':
    demonstrate()
