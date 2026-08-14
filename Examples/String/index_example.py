"""
index_example.py

Explain and demonstrate str.index(sub[, start[, end]]).
"""

EXPLANATION = """
s.index(sub) is like find() but raises ValueError if sub is not found.
It returns the lowest index where sub starts.
"""


def demonstrate():
    s = "abracadabra"
    print(EXPLANATION)
    print('s ->', s)
    print("s.index('ra') ->", s.index('ra'))
    try:
        print("s.index('z') ->", s.index('z'))
    except ValueError as e:
        print('Index raised:', e)


if __name__ == '__main__':
    demonstrate()
