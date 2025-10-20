#2. Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen

nimi = input('Anna nimi, enter lopettaa: ')
nimilista = []
while nimi != '':
    nimilista.append(nimi)
    nimi = input('Anna nimi, enter lopettaa: ')
    if nimi in nimilista:
        print(f'{nimi} on jo aiemmin syötetty')
    else:
        print('uusi nimi')

for i in nimilista:
    print(i)