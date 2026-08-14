"""
find_example.py

Explain and demonstrate str.find(sub[, start[, end]]).
"""

EXPLANATION = """
s.find(sub) returns the lowest index where substring sub is found,
or -1 if not found. Optional start and end restrict the search slice.
"""


def demonstrate():
    s = "Hello world, hello"
    print(EXPLANATION)
    print('s ->', repr(s))
    print("s.find('hello') ->", s.find('hello'))
    print("s.find('hello', 0, 12) ->", s.find('hello', 0, 12))
    print("s.find('x') ->", s.find('x'))


if __name__ == '__main__':
    demonstrate()
