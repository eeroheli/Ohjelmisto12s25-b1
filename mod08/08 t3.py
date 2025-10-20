#3. Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector

connection = mysql.connector.connect(
    port=3306,
    host='localhost',
    database='flight_game',
    user='---',
    password='----',
    autocommit=True
)
from geopy.distance import geodesic
haku1 = (input('anna ensimmäinen ICA0 koodi niin etsin kahden lentokentän etäisyyden: '))
haku2 = (input('anna toinen ICA0 koodi niin etsin kahden lentokentän etäisyyden: '))
def etaisyyslaskuri(eka, toka):
    kentta1 = (f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident like "{eka}"')
    cursor1 = connection.cursor()
    cursor1.execute(kentta1)
    result1 = cursor1.fetchone()
    kentta2 = (f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident like "{toka}"')
    cursor2 = connection.cursor()
    cursor2.execute(kentta2)
    result2 = cursor2.fetchone()
    tulos = geodesic(result1, result2).km
    return tulos

print(f'lentokenttien etäisyys toisitaan on: {etaisyyslaskuri(haku1, haku2):.2f} km ')
