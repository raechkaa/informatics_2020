import time


def counter(file):
    lines = 0
    for line in open(file):
        lines += 1
    return lines


files = ['1.txt', '2.txt', '3.txt']
start = time.time()
a = []
for i in range(len(files)):
    a.append(counter(files[i]))
print(time.time() - start)
print(a)
# время = 0.009021759033203125
# [40, 42, 46] - вывод
