#1. Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

heitot = int(input('Montako noppaa haluat heittää'))
n = 0
silmaluvut = []
while heitot > n:
    n = +1
    tulos = random.randint(1,6)
    silmaluvut.append(tulos)