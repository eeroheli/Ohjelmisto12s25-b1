#3. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
app_running = True
numerot = []
while app_running:
    luku = input('anna luku: ')
    if luku == '':
        app_running = False
    else :
        luku = float(luku)
        numerot.append(luku)

print(f'lukuesi suurin arvo on {max(numerot)} ,ja pienin {min(numerot)}')
