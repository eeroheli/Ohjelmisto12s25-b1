#3. Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku = float(input("Annna kokonaisluku: "))
itsellaan = luku % luku
yhedella = luku % 1
kahdella = luku % 2
kolmella = luku % 3
if yhedella == 0 and itsellaan == 0 and kahdella != 0 and kolmella != 0:
    print(f'luku {luku:.0f} on alkuluku')
else :
    print(f'luku {luku:.0f} ei ole alkuluku')
