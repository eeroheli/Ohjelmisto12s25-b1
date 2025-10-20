#4. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f(lista):
    print(sum(lista))
f(luvut)