import time
import threading


def thread_job(b):
    global result
    result += b


n = int(input())
a = []
result = 0
start = time.time()
for i in range(n):
    a.append(i)
print(a)
threads = [threading.Thread(target=thread_job(a[i])) for i in range(len(a))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(result)
print(time.time() - start)