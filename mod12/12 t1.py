#1. Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
import requests

pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto).json()
print(vastaus['value'])