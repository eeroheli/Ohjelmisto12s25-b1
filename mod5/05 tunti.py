
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