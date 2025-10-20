#6.
import random
#kaikkien pisteiden määrä N
N = int(input('montako pistettä arvotaan: '))
i = 0
n = 0
while i < N:
    i += 1
    #arvotaan satunnainen piste koordinaatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'arvottu piste: {x}, {y}')
    if (x ** 2 + y ** 2) < 1:
        n += 1
pi_likiarvo = 4 * n / N
print(f'piin likiarvo on: {pi_likiarvo}')
