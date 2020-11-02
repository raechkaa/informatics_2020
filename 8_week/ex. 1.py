def function(res):
    res = res ** 2
    return res


iterable = [1, 2, 3, 4]


def print_map(function, iterable):
    k = 0
    iterator = iter(iterable)

    while k < len(iterable):
        print(function(next(iterator)))
        k += 1


print_map(function, iterable)
