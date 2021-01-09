from multiprocessing import Pool
import time


def counter(file):
    lines = 0
    for line in open(file):
        lines += 1
    return lines


if __name__ == '__main__':
    pool = Pool(processes=4)
    start = time.time()
    print(pool.map(counter, ['1.txt', '2.txt', '3.txt']))
    print(time.time() - start)
# время = 0.25771117210388184
# вывод = [40, 42, 46]
# потому что я создала всего 3 файла и поэтому простая реализация эффективней чем с мультипроцессорами
