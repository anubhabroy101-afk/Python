"""
partition_example.py

Explain and demonstrate str.partition(sep).
"""

EXPLANATION = """
s.partition(sep) splits the string at the first occurrence of sep
and returns a 3-tuple: (before, sep, after). If sep is not found,
the tuple is (original, '', ''). This is useful when you need the
separator preserved or a single split.
"""


def demonstrate():
    s = 'user@example.com'
    print(EXPLANATION)
    print('s ->', s)
    print("s.partition('@') ->", s.partition('@'))
    print("s.partition('.') ->", s.partition('.'))
    print("'no-sep'.partition(',') ->", 'no-sep'.partition(','))


if __name__ == '__main__':
    demonstrate()
