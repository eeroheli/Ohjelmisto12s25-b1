import math
import random

#1.
käyttäjä = input('Terve mikä on nimesi: ')
print('Terve, ' + käyttäjä + '!')

#2.
#ymyrän ala = pi*r^2
ympyran_sade = float(input('Anna ympyrän säde :'))
ympyran_pintaala = math.pi * ympyran_sade ** 2
print(f'ympyrän pinta-ala on: {ympyran_pintaala:.2f}')

#3. suorakulmion laskeminen
#kysytään arvot
suorakulmion_kanta = float(input('Anna suorakulmion kanta :'))
suorakulmion_korkeus = float(input('Anna suorakulmion korkeus :'))

#lasketaan
suorakulmion_piiri = suorakulmion_kanta + suorakulmion_kanta + suorakulmion_korkeus + suorakulmion_korkeus
suorakulmion_pintaala = suorakulmion_kanta * suorakulmion_korkeus

print(f'Suorakulmion piiri on : {suorakulmion_piiri:.2f}')
print(f'Suorakulmion pinta-ala on : {suorakulmion_pintaala:.2f}')

#4. kolme lukua
#kysytään arvot
luku1 = float(input('Anna luku 1 :'))
luku2 = float(input('Anna luku 2 :'))
luku3 = float(input('Anna luku 3 :'))

#lasketaan lukujen summa tulo ja keskiarvo
lukujen_summa = luku1 + luku2 + luku3
lukujen_tulo = luku1 * luku2 * luku3
lukujen_keskiarvo = (luku1 + luku2 + luku3) / 3

print(f'lukujen summa on : {lukujen_summa:.2f}')
print(f'lukujen tulo on : {lukujen_tulo:.2f}')
print(f'lukujen keskiarvo on : {lukujen_keskiarvo:.2f}')

#5 keskiajan painot

#kysytään arvot
leiviska = float(input('Anna leivisköjen määrä :'))
naula = float(input('Anna naulojen määrä :'))
luoti = float(input('Anna luotien määrä :'))

#6. pin koodi

pin11 = random.randint(0, 9)
pin12 = random.randint(0, 9)
pin13 = random.randint(0, 9)
pin21 = random.randint(0, 6)
pin22 = random.randint(0, 6)
pin23 = random.randint(0, 6)
pin24 = random.randint(0, 6)

print(f'3 numeroinen pin koodi on : {pin11} {pin12} {pin13}')
print(f'4 numeroinen pin koodi on : {pin21} {pin22} {pin23} {pin24}')
