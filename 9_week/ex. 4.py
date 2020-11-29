import random
import math

def sample_coroutine():
    x = 0
    sum = 0
    sum_kv = 0
    kol = 0
    while True:
        sum += x
        sum_kv += x**2
        kol += 1
        x = yield 'avr:', round(sum/kol, 1), 'kol:', kol-1, 'dsp:', round(0.1*sum_kv - (.1*sum)*2, 2)
   

cor = sample_coroutine()
next(cor)
for i in range(10):
    zn = random.randint(1,100)
    print(cor.send(zn))
