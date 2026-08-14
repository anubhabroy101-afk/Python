"""
removesuffix_example.py

Explain and demonstrate str.removesuffix(suffix) (Python 3.9+).
"""

EXPLANATION = """
s.removesuffix(suffix) returns a new string with the suffix removed
if present; otherwise returns the original string unchanged. Useful
for file extensions or predictable endings.
"""


def demonstrate():
    s = 'file.txt'
    print(EXPLANATION)
    print('s ->', s)
    print("s.removesuffix('.txt') ->", s.removesuffix('.txt'))
    print("'nope'.removesuffix('.txt') ->", 'nope'.removesuffix('.txt'))


if __name__ == '__main__':
    demonstrate()
