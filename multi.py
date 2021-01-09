from multiprocessing import Pool
import time


def counter(file):
    lines = 0
    for line in open(file):
        lines += 1
    return lines


if __name__ == '__main__':
    pool = Pool(processes=5)
    files_len = 1000
    start = time.time()
    print(pool.map(counter, ["./{}.txt".format(i) for i in range(files_len)]))
    print(time.time() - start)
# время = 0.25771117210388184
# вывод = [40, 42, 46]
# потому что я создала всего 3 файла и поэтому простая реализация эффективней чем с мультипроцессорами
# для 1000 файлов время = 0.17364239692687988
