"""
replace_example.py

Explain and demonstrate str.replace(old, new[, count]).
"""

EXPLANATION = """
s.replace(old, new, count) returns a copy of the string with all
occurrences of the substring old replaced by new. If count is provided,
only the first count occurrences are replaced.
"""


def demonstrate():
    s = "banana"
    print(EXPLANATION)
    print('s ->', repr(s))
    print("s.replace('a', 'A') ->", s.replace('a', 'A'))
    print("s.replace('a', '-', 2) ->", s.replace('a', '-', 2))


if __name__ == '__main__':
    demonstrate()
