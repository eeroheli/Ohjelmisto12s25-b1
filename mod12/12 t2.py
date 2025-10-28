# 2. Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import requests
import json
paikkakunta = input('anna paikkakunnan nimi: ')
pyynto1 = f'http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=5&appid=26e95cc1408994e6db89afaf8ef94370'
vastaus1 = requests.get(pyynto1).json()
pyynto2 = f'https://api.openweathermap.org/data/2.5/weather?lat={vastaus1[0]["lat"]}&lon={vastaus1[0]["lon"]}&appid=26e95cc1408994e6db89afaf8ef94370&units=metric&lang=fi'
vastaus2 = requests.get(pyynto2).json()


saa = vastaus2['main']['temp'] - 273.15
print(f'{paikkakunta} paikkakunnalla on {vastaus2['main']['temp']:.2f} astetta lämmintä ja säätä kuvaillaan: {vastaus2['weather'][0]['description']}')
