"""
isupper_example.py

Explain and demonstrate str.isupper().
"""

EXPLANATION = """
s.isupper() returns True if the string contains at least one cased
character and all such cased characters are uppercase. Non-cased
characters are ignored.
"""


def demonstrate():
    samples = ["ABC", "ABC123", "AbC", "123", ""]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.isupper()}')


if __name__ == '__main__':
    demonstrate()
