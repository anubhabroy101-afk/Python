"""
join_example.py

Explain and demonstrate str.join(iterable).
"""

EXPLANATION = """
separator.join(iterable) concatenates the elements of the iterable
(using the separator string between elements). Every item in the iterable
must already be a string.
"""


def demonstrate():
    parts = ['one', 'two', 'three']
    sep = '-'
    print(EXPLANATION)
    print('parts ->', parts)
    print("'-'.join(parts) ->", sep.join(parts))
    # join with generator
    print("','.join(x.upper() for x in parts) ->", ','.join(x.upper() for x in parts))


if __name__ == '__main__':
    demonstrate()
