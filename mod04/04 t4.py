#4.Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

app_running = True
satunnainen_luku = random.randint(1, 10)
while app_running:
    arvaus = int(input('arvaa luku: '))
    if arvaus > satunnainen_luku:
        print('lukusi on liian suuri')
    elif arvaus < satunnainen_luku:
        print('lukusi on liian pieni')
    else :
        print('lukusi on oikein!')
        app_running = False
