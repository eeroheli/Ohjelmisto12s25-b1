#2. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numero = input('Anna luku, Enter lopettaa: ')
luvut = []
luvut.append(numero)
while numero != '' :
    numero = input('Anna luku, Enter lopettaa: ')
    luvut.append(numero)
luvut.sort(reverse=True)
for n in range(5):
    print(luvut[n])