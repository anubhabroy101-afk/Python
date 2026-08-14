"""
islower_example.py

Explain and demonstrate str.islower().
"""

EXPLANATION = """
s.islower() returns True if the string contains at least one cased
character and all such cased characters are lowercase. Non-cased
characters are ignored.
"""


def demonstrate():
    samples = ["abc", "abc123", "Abc", "123", ""]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.islower()}')


if __name__ == '__main__':
    demonstrate()
