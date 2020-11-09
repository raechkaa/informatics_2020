import itertools


def get_combinations(s, n):
    arr = []
    for i in range(1, n+1):
        for k in itertools.combinations(s, i):
            arr.append(''.join(k))
    arr.sort()
    return arr


print(get_combinations("cat", 2))

