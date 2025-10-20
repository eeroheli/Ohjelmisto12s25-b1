#6. Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
pizza1 = float(input('anna ensimmäisen pizzan halkaisija senttimetreinä: '))
hinta1 = float(input('anna ensimmäisen pizzan hinta euroina: '))
pizza2 = float(input('anna toisen pizzan halkaisija senttimetreinä: '))
hinta2 = float(input('anna toisen pizzan hinta euroina: '))
def pizzalaskuri(pizza, hinta):
    säde = pizza / 2
    pizzacm = math.pi * (säde ** 2)
    pizzam = pizzacm / 10000
    yhinta = (hinta/pizzam)
    return yhinta

if pizzalaskuri(pizza1, hinta1) > pizzalaskuri(pizza2, hinta2):
    print('toinen pizza on halvempi')
elif pizzalaskuri(pizza1, hinta1) < pizzalaskuri(pizza2, hinta2):
    print('ensimmäinen pizza on halvempi')
else :
    print('pizzat ovat samanhintaisia')
