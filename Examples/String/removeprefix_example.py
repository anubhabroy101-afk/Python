"""
removeprefix_example.py

Explain and demonstrate str.removeprefix(prefix) (Python 3.9+).
"""

EXPLANATION = """
s.removeprefix(prefix) returns a new string with the prefix removed
if present; otherwise returns the original string unchanged. This is
preferable to slicing checks because it's explicit and readable.
"""


def demonstrate():
    s = 'pre_hello'
    print(EXPLANATION)
    print('s ->', s)
    print("s.removeprefix('pre_') ->", s.removeprefix('pre_'))
    print("'nope'.removeprefix('pre_') ->", 'nope'.removeprefix('pre_'))


if __name__ == '__main__':
    demonstrate()
