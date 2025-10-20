# MONIKKO

# Monikko eli (tuple) on kuin lista jota ei voi muokata.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

monikko = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#monikko2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 voi tehdä ilman sulkuja mutta tapana sulkujen kanssa selvyyden takia
print(monikko)

# voi sisältää ei tietoa
monikko2 = (1, 2, 'yea', 'eero', (3, 4), 5)
print(monikko2)

# luetaan listan ja monikon eka alkio samalla tavalla
print(lista[0])
print(monikko2[0])

# Monikkoa ei voi muokata, listaa voi
lista[0] = 0
lista.append(11)
print(f'muokattu lista on {lista}')
print('-------------------------------------')
#monikko[0] = 0 ei toimi ei voi muokata

'''
print('----------------------------')
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.
'''

#monikon läpikäynti kuten listan
sanat = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')
for i in sanat:
    print(i)
    if i == 'kolmas':
        print('sana kolmas löytyi')

if 'viides' in sanat:
    print('sana viides löytyi')

#moniko arvojen purku muuttujiin
hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")

#monikon voi antaa funktiolle parametrina

def tulosta_monikko(monikko):
    for i in monikko:
        print(i)

tulosta_monikko(hedelmät)
print('--------------------------------------')
#monikko funktion paluuarvona
import random
#perinteinen
def heita():
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    print(f'heitit {noppa1}, ja  {noppa2}')
heita()
#yksikertaistetaan
def heita2():
    #luodaan monikko joka puretaan muuttujiin
    (eka1, toka1) = (random.randint(1, 6), random.randint(1, 6))
    print(f'heitit {eka1}, ja  {toka1}')
heita2()
# monikko myös paluuarvona
def heita3():
    #luodaan monikko joka puretaan muuttujiin
    (eka1, toka1) = (random.randint(1, 6), random.randint(1, 6))
    return eka1, toka1
noppa1, noppa2 = heita3()
print(f'funktiosta heita3 palautui {noppa1}, ja  {noppa2}')

print('---------------------------------------')
print('joukko\n')
#JOUKKO eli set {}
# järjestymätön tietorakenne missä tahansa järjestyksessä vain uniikkeja arvoja ei voi viitata
joukko = {1, 2, 3, 4, 5, 6} # merkataan aaltosulkeilla
print(joukko)

llista = [1, 2, 3, 4, 5, 6, 6]
mmonikko = (1, 2, 3, 4, 5, 6, 6)
jjoukko = {1, 2, 3, 4, 5, 6, 6} # sama luku ei voi esiintyä useasti
print(jjoukko)

jjoukko.add(6) # ei virhettä mutta ei lisäänny koska on jo
jjoukko.add(7)
print(jjoukko)
jjoukko.remove(6)
print(jjoukko)

pelit = {"Monopoli", "Shakki", "Cluedo", "Muuttuva labyrintti"}
print(pelit)

for p in pelit:
    print(p)

if 'Cluedo' in pelit:
    print('löytyy')

# tyhjän lista luomien
autolista = []
autolista.append('Audi')
print(autolista)
print(type(autolista))

#tyhjä joukko luodaan set funktiolla
autojoukko = set()
autojoukko.add('Mersu')
print(autojoukko)
print(type(autojoukko))

# jos ei käytä set tulee sanakirja
autosanakirja = {}
print(type(autosanakirja))

print('SANAKIRJA\n')
print('-------------------------')
#SANAKIRJA (dictionary) on käytetyimipiä tietorakenteita
# voidaan tallentaa avain-arvopaperja
# kuntsanakirja alustetaan annetaan avain-arvopari seuraavasti: AVAIN : ARVO
# peräkkäiset erotellaan pilkulla
oppilaat = {'Aapeli' : 25, 'Bertta' : 56, 'Cecilia' : 53, 'Daniel' : 23, 'Emma' : 25}
print(oppilaat)
# mitä ovat tietueet ja items
print(oppilaat.items())

# mitä on avaimet
print(oppilaat.keys())

# mitä on arvot / values
print(oppilaat.values())

#käydään läpri for rakenteella
# kierrosmuuttja saa arvokseen saa vain avaimen
for i in oppilaat:
    print(i)

avain = 'Aapeli'
oppilaat[avain]
print('etsitään avaimella aapeli ja hänen ikä', oppilaat[avain])
print('danielin ikä on ', oppilaat['Daniel'])

for i in oppilaat:
    print(f'oppilaan nimi on {i}, ja ika {oppilaat[i]}')
# hae haluttu ika if in  käyttäen
nimi = input('anna nimi jota etsin: ')
if nimi in oppilaat:
    print(f'nimi {nimi} löytyi ja sen ika on {oppilaat[nimi]}')
else:
    print(f'nimeä {nimi} ei löydy')
yhteystiedot = {'Aapeli' : {'puh' : '053213'} , 'Bertta' : {'puh' : '02021033'}, 'Cecilia' : {'puh' : '0532332113'}}
print(yhteystiedot)