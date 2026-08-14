"""
lower_example.py

Explain and demonstrate str.lower().
"""

EXPLANATION = """
s.lower() returns a copy of the string with all cased characters
converted to lowercase. Does not affect non-cased characters.
"""


def demonstrate():
    samples = ["ABC", "MiXeD Case 123", "ß"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {repr(s.lower())}')


if __name__ == '__main__':
    demonstrate()
