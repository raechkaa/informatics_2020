import time
import threading


def thread_job(file):
    lines = 0
    for line in open(file):
        lines += 1


files_len = 1000
files = []
for i in range(files_len):
    files.append("./{}.txt".format(i))
start = time.time()
a = []
threads = [threading.Thread(target=thread_job(files[i])) for i in range(len(files))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)  # время = 0.9820380210876465
