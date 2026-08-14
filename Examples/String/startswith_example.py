"""
startswith_example.py

Explain and demonstrate str.startswith(prefix[, start[, end]]).
"""

EXPLANATION = """
s.startswith(prefix) returns True if the string begins with prefix.
prefix may be a tuple of prefixes to check any of them. Optional start/end
can limit the checked slice.
"""


def demonstrate():
    s = 'hello.py'
    print(EXPLANATION)
    print('s ->', s)
    print("s.startswith('he') ->", s.startswith('he'))
    print("s.startswith(('h','x')) ->", s.startswith(('h','x')))


if __name__ == '__main__':
    demonstrate()
