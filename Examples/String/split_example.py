"""
split_example.py

Explain and demonstrate str.split(sep=None, maxsplit=-1).
"""

EXPLANATION = """
s.split() with no sep splits on any whitespace and discards leading
and trailing whitespace. With sep specified, the split is exact and
empty strings can appear in the result. maxsplit limits the number of
splits performed.
"""


def demonstrate():
    s1 = 'one two  three\n'
    s2 = 'a,b,,c'
    print(EXPLANATION)
    print('s1.split() ->', s1.split())
    print('s2.split(",") ->', s2.split(','))
    print('s2.split(",", 2) ->', s2.split(',', 2))


if __name__ == '__main__':
    demonstrate()
