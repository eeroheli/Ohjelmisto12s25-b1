#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
from flask_cors import CORS
import mysql.connector
connection = mysql.connector.connect(
    port=3306,
    host='localhost',
    database='flight_game',
    user='eero',
    password='yeah123',
    autocommit=True
)


app = Flask(__name__)
CORS(app)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    cursor1 = connection.cursor()
    cursor1.execute(f'SELECT name, municipality FROM airport WHERE ident like "{icao}"')
    result1 = cursor1.fetchall()
    vastaus = {
        'ICAO': icao,
        'Name': result1[0][0],
        'municipality': result1[0][1]
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3001)