#5. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
lukujono = [1, 423, 24, 45,  22, 64]
def f(jono):
    jono2 = jono.copy()
    for x in jono:
        if x % 2 != 0:
            jono2.remove(x)
    return jono2
print(f'alkuperäinen lista on {lukujono} ja karsittu on {f(lukujono)}')
