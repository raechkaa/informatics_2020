import itertools


def compress_string(s):
    result = []
    for k, g in itertools.groupby(s):
        result += [(int(sum(1 for i in g)), int(k))]
    return result


print(compress_string('1222311'))
