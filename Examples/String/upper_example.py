"""
upper_example.py

Explain and demonstrate str.upper().
"""

EXPLANATION = """
s.upper() returns a copy of the string with all cased characters
converted to uppercase.
"""


def demonstrate():
    samples = ["abc", "MiXeD Case 123", "ß"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {repr(s.upper())}')


if __name__ == '__main__':
    demonstrate()
