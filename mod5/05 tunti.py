from itertools import count

nimi1 = 'Ula'
nimi2 = 'Matti'
num1 = 45
num2 = 56
print(f'Hei {nimi1} ikäsi on {num1}')

#tyhjä lista
lista = []

#lista voi sisätää muuttujia numeroita jne
nimet = ['Anna', 'liisa', nimi1, nimi2, 'Toni', 'Ilkka']
print(nimet)

#lista voi sisätää toisia listoja
ikalista = [24, 38, 34, [45, 87, 99]]
print(ikalista)

#listan pituuden voi katsoa len komennola
print(len(nimet))

lista1 = [34, 25, 18, 'eero']
print(len(lista1))

#listasta voidaan hakea tietoa indeksin avula TAI viipaloinnila
#alkioon viitataan indeksinumerola alkaen numerosta 0 viimeinen on -1
print(f'Hei {nimet[0]} ja terve myös {nimet[4]}!')

print(ikalista[3][1])
print(len(ikalista[3]))

#tapoja viitata listan alkioihin
nimet2 = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Anna", "Pasi", "jyri"]
print(nimet2[3])
print(nimet2[2:6])
print(nimet2[-1])
print(nimet2[2:])
print(nimet2[1:-1])
print(nimet2[0:-1:2])
print('---------------------------------')

#uusi lista = vanha lista[alku:loppu:askel]

uusi_lista = nimet2[2:4]
print(nimet2)
print(uusi_lista)

#lista jossa 5 kaupunkia tulosta niistä kolme ensimmäistä ja viimeinen
kaupungit = ['helsinki', 'espoo', 'kirkkonummi', 'vantaa', 'lapua']
print(f'{kaupungit[0:3]} ja {kaupungit[4]}')
print(kaupungit[3])
print('---------------------------------------------')

kaupungit.append('Uusi kaupinki')
print(kaupungit)
if 'lapua' in kaupungit:
    print('lapua löytyi ja poistetaan se')
    #poistetaan kaupunki
    kaupungit.remove('lapua')
    print(kaupungit)
kaupungit.insert(0, 'lapua')
print(kaupungit)

#tutkitaan monesko indeksi
monesko = kaupungit.index('lapua')
print(monesko)

lisaa_kaupunkeja = ['Tampere', 'Kotka']
kaupungit.extend(lisaa_kaupunkeja)
print(kaupungit)

#muokataan olemassa olevaa alkiota
kaupungit[7] = 'Sipoo'
print(kaupungit)

hedelmat = ['appelsiini', 'greippi', 'Banaani']
numerolista = [69, 120, 12]
hedelmat.sort()
print(hedelmat)
numerolista.sort(reverse=True)
print(numerolista)

viikonpaivat = ['Maanantai', 'Tiistai']
print(viikonpaivat)

print(type(viikonpaivat))

print('------------------------------------')
print('muutamia hyödylisiä funkitota')
print('------------------------------------')

#listoile täläiset funktiot
# len, sum, min, max, count
luvut = [4, 6, 1, 5, 2, 9]
print(len(luvut)) # pituus
print(sum(luvut)) # lukujen summa
print(min(luvut)) # pienin numero
print(max(luvut)) # suurin numero
print(luvut.count(5)) # kuinka monta 5 on listassa
print('-----------------------------------------------')
#miten käydään lista läpi iteroimala
i = 0
while i < len(luvut):
    print(luvut[i])
    i = i + 1
print('----------------------------------')
# käydään lista läpi alkio alkiolta
for numero in luvut:
    print(numero)

print('----------------------------------')
for kirjain in 'abcdefg':
    print(kirjain)

print('----------------------------------')
for alkio in [1, 2, 3, 4, 5, 6]:
    print(alkio)
print('----------------------------------')
# tässä tapauksessa kaupunki on kierrosmuuttuja
for kaupinki in kaupungit:
    print(kaupinki)
print('----------------------------------')
for numero1 in range(4, 80, 4):
    print(numero1)
print('----------------------------------')
for nu in range(80, 10, -1):
    print(nu)
print('----------------------------------')
pituus = len(luvut)
for n in range(pituus):
    print(luvut[n])
for n in range(3):
    print(kaupungit[n])