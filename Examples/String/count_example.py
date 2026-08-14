"""
count_example.py

Explain and demonstrate str.count(sub[, start[, end]]).
"""

EXPLANATION = """
s.count(sub) returns the number of non-overlapping occurrences of sub
in the string (optionally restricted by start and end indices).
"""


def demonstrate():
    s = 'banana'
    print(EXPLANATION)
    print('s ->', s)
    print("s.count('a') ->", s.count('a'))
    print("s.count('an') ->", s.count('an'))


if __name__ == '__main__':
    demonstrate()
