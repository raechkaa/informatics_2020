import itertools


def get_permutations(s, n):
    array = []
    arr = list(itertools.permutations(s, n))
    arr.sort()
    result = list(map(list, arr))
    for i in range(len(result)):
        array.append(result[i][0] + result[i][1])
    return array


a = "cat"
b = 2
print(get_permutations(a, b))