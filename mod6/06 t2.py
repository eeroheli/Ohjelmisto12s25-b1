#2. Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

tahkot = int(input('tahkojen määrä: '))
def heita():
    luku = random.randint(1, tahkot)
    return luku

heitto = 0
while heitto < tahkot:
    heitto = heita()
    print(f'heitto oli: {heitto}')