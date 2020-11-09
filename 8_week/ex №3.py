import itertools


def get_combinations(s, n):
    arr = []
    for i in range(1, n+1):
        for item in itertools.combinations(s, i):
            arr.append(''.join(item))
    arr.sort()
    return arr


print(get_combinations("cat", 2))

