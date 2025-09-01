#1. Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

heitot = int(input('Montako noppaa haluat heittää: '))
silmaluvut = []
for i in range(heitot):
    tulos = random.randint(1,6)
    silmaluvut.append(tulos)
print(silmaluvut)
print(sum(silmaluvut))