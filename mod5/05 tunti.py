
nimi1 = 'Ulla'
nimi2 = 'Matti'
num1 = 45
num2 = 56
print(f'Hei {nimi1} ikäsi on {num1}')

#tyhjä lista
lista = []

#lista voi sisätää muuttujia numeroita jne
nimet = ['Anna', 'Liisa', nimi1, nimi2, 'Toni', 'Ilkka']
print(nimet)

#lista voi sisätää toisia listoja
ikalista = [24, 38, 34, [45, 87, 99]]
print(ikalista)

#listan pituuden voi katsoa len komennolla
print(len(nimet))

lista1 = [34, 25, 18, 'eero']
print(len(lista1))

#listasta voidaan hakea tietoa indeksin avulla TAI viipaloinnilla
#alkioon viitataan indeksinumerolla alkaen numerosta 0 viimeinen on -1
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

viikonpaivat =