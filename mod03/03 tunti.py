#
import random

satunnaisluku = random.randint(0,100)

print(f'arvottu luku: {satunnaisluku}')
# kolikonheittosimulaattori
if satunnaisluku < 50:
    print("kruuna!")
elif satunnaisluku > 50:
    print("klaava!")
else:
    print("kolikko jäi pystyyn!")

#Dummy-kirjautuminen
oikea_salasana = 'salakala'
oikea_tunnus = 'eero'
input_tunnus = input('anna tunnus: ')
input_salasana = input('anna salasana: ')
if input_salasana == oikea_salasana and input_tunnus == oikea_tunnus:
    print('Tervetuloa!')
    kehote = input('mitäs haluat tehdä? ')
    if kehote == 'tervehtiä':
        print('Terve!')
    else:
        print('en ymmärtänyt')
else :
    print('Väärä salasana!')

print('ohjelma suljettu. ')
