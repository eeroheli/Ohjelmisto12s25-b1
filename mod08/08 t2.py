#2. Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import mysql.connector

connection = mysql.connector.connect(
    port=3306,
    host='localhost',
    database='flight_game',
    user='eero',
    password='yeah123',
    autocommit=True
)
haku = (input('anna maakoodi: '))
cursor = connection.cursor()
cursor.execute(f'SELECT type, count(*) FROM airport WHERE iso_country like "{haku}" GROUP BY type')
result = cursor.fetchall()
if result == []:
    print('annoit väärän koodin')
else:
    print(result)
