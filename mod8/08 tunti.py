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

#print(connection) testaa toimiiko
# luodaan osoitin ja sijoittaa vittaus siihen muuttujaan
cursor = connection.cursor()
#käytetään osoitinta tietokantahakuun
cursor.execute('SELECT name, iso_country FROM country')
# haetaan tulosjoukosta rivi kerrallaan
result = cursor.fetchone()
print(result)
result = cursor.fetchone()
print(result)
result = cursor.fetchmany(3)
print(result)
# yleisin tapa haetaan kaikki (loput) tulokset
result = cursor.fetchall()
print(f' listan pituus {len(result)}')
#tulostetaan enimmäisen rivin maakoodi
print(result[0][1])

# tulostetaan tulosjoukko muotoituna
for i in result:
    print(f'maan {i[0]} maakoodi on {i[1]}')
print('----------------------------')

def get_country_name_by_code(code):
    maa = (f'SELECT name FROM country WHERE iso_country like "{code}"')
    cursor1 = connection.cursor()
    cursor1.execute(maa)
    result1 = cursor1.fetchone()
    if result1 == None:
        return "ei löydy"
    return result1[0]
maakoodi = input('anna maakoodi: ')

print(f'annetun maakoodin {maakoodi} maa on: {get_country_name_by_code(maakoodi)}')
