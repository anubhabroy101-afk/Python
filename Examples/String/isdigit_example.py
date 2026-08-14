"""
isdigit_example.py

Explain and demonstrate str.isdigit().
"""

EXPLANATION = """
s.isdigit() returns True if the string is non-empty and all characters
are digits. Note: some unicode numerals count as digits as well.
"""


def demonstrate():
    samples = ["12345", "Ⅻ", "12.3", "", "٤٥٦"]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.isdigit()}')


if __name__ == '__main__':
    demonstrate()
