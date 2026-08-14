"""
len_example.py

Explain and demonstrate Python's built-in len() when used with strings.
"""

EXPLANATION = """
len(s) returns the number of characters in the string s.
It counts Unicode code points in Python's str type (not bytes). Use len(s.encode(...))
if you need the encoded byte length.
"""


def demonstrate():
    s = "Hello"
    s_ws = "  Hi \n"
    empty = ""

    print(EXPLANATION)
    print('len("Hello") ->', len(s))
    print('len("  Hi \n") ->', len(s_ws), '(includes spaces and newline)')
    print('len("") ->', len(empty), '(empty string has length 0)')
    print('Byte-length of "€" in UTF-8 ->', len('€'.encode('utf-8')))


if __name__ == '__main__':
    demonstrate()
