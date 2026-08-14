"""
isspace_example.py

Explain and demonstrate str.isspace().
"""

EXPLANATION = """
s.isspace() returns True if the string is non-empty and all characters
are whitespace (spaces, tabs, newlines and other Unicode whitespace).
"""


def demonstrate():
    samples = ["   ", "\n\t", "a b", ""]
    print(EXPLANATION)
    for s in samples:
        print(f'{repr(s)} -> {s.isspace()}')


if __name__ == '__main__':
    demonstrate()
