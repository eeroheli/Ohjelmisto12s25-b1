#2. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numero = input('Anna luku, Enter lopettaa: ')
luvut = []
while numero != '' :
    numero = int(numero)
    luvut.append(numero)
    numero = input('Anna luku, Enter lopettaa: ')
luvut.sort(reverse=True)
for n in range(5):
    print(luvut[n])