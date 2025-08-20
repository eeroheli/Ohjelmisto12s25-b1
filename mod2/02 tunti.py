    #20.8

"""
monirivinen kommentti
"""

import math
import random

nimi = input('mikä on nimesi: ')    #palauttaa merkkijonon (str)
ika = 20    #kokonaisluku (int)
ika_ensi_vuonna = ika + 1
str_ika_ensi_vuonna = str(ika_ensi_vuonna)

tervehdys = 'moi ' + nimi + ' ' + str_ika_ensi_vuonna

print(tervehdys)

#simppeli laskukone

#luetaan käyttäjältä kaksi lukua muutetaan samantien liukuluvuiksi
luku1 = float(input('anna ensimmäinen luku '))
luku2 = float(input('anna toinen luku '))

#lasketaan tulos
#tulos = int(luku1) + int(luku2)  #kokonaisluvuilla
tulos_yhteenlasku = luku1 + luku2  #kokonaisluvuilla
tulos_vahennyslasku = luku1 - luku2  #kokonaisluvuilla
tulos_kertolasku = luku1 * luku2
tulos_jakolasku = luku1 / luku2
tulos_kokonaisosa = luku1 // luku2
tulos_jakojaannos = luku1 % luku2
tulos_potensiinkorotus = luku1 ** luku2

print('yhteenlaskutoimituksen tulos: ' + str(tulos_yhteenlasku))
print('vähennyslaskun tulos: ' + str(tulos_vahennyslasku))
print('kertolaskun tulos: ' + str(tulos_kertolasku))
#tuloksen muotoilu f stringillä
print(f'jakolaskun tulos: {tulos_jakolasku:.2f}, jossa kokonaisosa on ' f'{tulos_kokonaisosa} ja jakojäännös {tulos_jakojaannos} ')
print(f'potenssiinkorotuksen tulos: {tulos_potensiinkorotus:.2f}')

#ymyrän ala = pi*r^2
#piin arvo
print(math.pi)

#satunnaisluvun generointi väliltä
print(random.randint(1, 6))

#6 satunnainen pin koodi
print('kolminumeroinen pin koodi on : ' random.randint(0, 9) ' ' random.randint(0, 9) ' ' random.randint(0, 9))
print('nelinumeroinen pin koodi on : ' random.randint(0, 6) ' ' random.randint(0, 6) ' ' random.randint(0, 6) ' ' random.randint(0, 6))