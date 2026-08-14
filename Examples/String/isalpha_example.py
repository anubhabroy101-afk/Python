"""
isalpha_example.py

Explain and demonstrate str.isalpha().
"""

EXPLANATION = """
s.isalpha() returns True when the string is non-empty and every
character is an alphabetic character (letters). It returns False for
digits, spaces or punctuation.
"""


def demonstrate():
    samples = ["Python", "py3", "", "naïve"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.isalpha()}')


if __name__ == '__main__':
    demonstrate()
