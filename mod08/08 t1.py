#1. Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector
#otetaan tietokanta yhteys
connection = mysql.connector.connect(
    port=3306,
    host='localhost',
    database='flight_game',
    user='eero',
    password='yeah123',
    autocommit=True
)
haku = (input('anna ICA0 koodi niin etsin vastaavan lentokentän: '))
cursor = connection.cursor()
cursor.execute(f'SELECT name, municipality FROM airport WHERE ident like "{haku}"')
result = cursor.fetchall()
if result == []:
    print('annoit väärän koodin')
else:
    print(result)
