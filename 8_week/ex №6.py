import itertools


def maximize(lists, m):
    array = []
    for i in range(len(lists)):
        array.append(max(lists[i]) **2)
    mass = list(itertools.accumulate(array))
    return mass[len(mass)-1] % m


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]

print(maximize(lists, m=1000))
