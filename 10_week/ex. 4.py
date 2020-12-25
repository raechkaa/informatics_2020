# время, вычисленное с помощью потоков = 2.901669502258301
# время, вычисленное без потоков = 2.526888847351074

import urllib.request
import time
import threading


def thread_job(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
urls = [
        'https://www.yandex.ru', 'https://www.google.com',
        'https://habrahabr.ru', 'https://www.python.org',
        'https://isocpp.org',
    ]
threads = [threading.Thread(target=thread_job(urls[i])) for i in range(len(urls))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)
