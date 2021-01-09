import time


def counter(file):
    lines = 0
    for line in open(file):
        lines += 1
    return lines


files_len = 1000
files = []
for i in range(files_len):
    files.append("./{}.txt".format(i))
start = time.time()
a = []
for i in range(len(files)):
    a.append(counter(files[i]))
print(time.time() - start)
print(a)
# время = 0.009021759033203125
# [40, 42, 46] - вывод
# для 1000 файлов время = 0.1306898593902588
