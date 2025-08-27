#6.
import random
#kaikkien pisteiden määrä N
N = 10
i = 0
n = 0
# Todo: kysy n arvo käyttäjältä
while i < N:
    i += 1
    #arvotaan satunnainen piste koordinaatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'arvottu piste: {x}, {y}')
    # TODO: testaaa toteuttaako epäyhtälön x^2+y^2<1
    # jos ehto totta nosta n laskurin arvoa

# TODO: laske ja tulosta piin likiarvo käyttäen π≈4n/N