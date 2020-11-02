import itertools


def get_cartesian_product(a, b):
    return list(itertools.product(a,b))


a = [1, 2, 3, 4]
b = [5, 6]
print(get_cartesian_product(a, b))
