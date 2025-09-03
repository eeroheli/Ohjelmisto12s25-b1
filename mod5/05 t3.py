#3. Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Annna kokonaisluku: "))
kokonaisluku = True
if luku < 2: #alle 2 luvut eivät ole alkulukuja
    kokonaisluku = False
for i in range(2, luku):
    if luku % i == 0:
        kokonaisluku = False

if kokonaisluku:
    print(f'luku {luku} on alkuluku')
else :
    print(f'luku {luku} ei ole alkuluku')
