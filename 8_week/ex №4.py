import itertools


def get_combinations_with_r(s, n):
    arr = []
    for i in itertools.combinations_with_replacement(s, n):
        arr.append(''.join(i))
    arr.sort()
    return arr


print(get_combinations_with_r("cat", 2))
