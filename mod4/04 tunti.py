#toistolause eli silmukka while

'''
suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print('totta')
    print('on vain kerran')

print('loppu')
'''

import random

#iteraattori ja while
toistojen_lkm = 10
i = 0

while i < toistojen_lkm :
    i = i + 1
    #i += 1 nopeampi
    print(f'iteroiva silmukka, i:n arvo {i}')

print(f'i:n arvo lopuksi {i}')


# Komentokehotesovellus ja laskukone
app_running = True
#main loop
while app_running:
    command = input('komento-> ')
    print(f'komentosi oli: {command}')
    if command == 'lopeta':
        app_running = False
    elif command == 'laskukone':
        luku1 = float(input('anna ensimmäinen luku '))
        luku2 = float(input('anna toinen luku '))
        tulos_yhteenlasku = luku1 + luku2
        print('yhteenlaskun tulos: ' + str(tulos_yhteenlasku))

#kolikonheitto n kertaa

n = 10000
i1 = 0
kolikko_pystyssa_lkm = 0
while i1 < n:
    satunnaisluku = random.randint(0, 1000)
    i1 = i1 + 1
    if satunnaisluku < 500:
        print("kruuna!")
    elif satunnaisluku > 500:
        print("klaava!")
    else:
        print("kolikko jäi pystyyn!")
        kolikko_pystyssa_lkm += 1
print(f'kolikko oli pystyssa {kolikko_pystyssa_lkm} kertaa')


#noppaesim
app_running = True
pelikerrat = 0
heittojen_lkm = 0
while app_running:
    noppa1 = noppa2 = heitot = 0
    while noppa1!=6 or noppa2!=6:
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    print(f"kahteen kutoseen tarvittiin {heitot:d} heittoa.")
    pelikerrat = pelikerrat + 1
    heittojen_lkm = heittojen_lkm + heitot
    komento = input('pelataanko uudestaan k/e ')
    if komento != 'k':
        app_running = False
print(f'Kaksi kutosta saatiin keskimäärin {heittojen_lkm/pelikerrat} heitolla.')