#4. Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeus):
        self.nopeusnyt = self.nopeusnyt + nopeus
        if self.nopeusnyt >= self.huippunopeus:
            self.nopeusnyt = self.huippunopeus
        elif self.nopeusnyt <= 0:
            self.nopeusnyt = 0

    def kulje(self, aika):
        self.kuljettumatka = aika * self.nopeusnyt
#luodaan lista
autot = []
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

game_running = True
while game_running:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettumatka >= 10000:
            print(f"{auto.rekisteritunnus} voitti kisan")
            game_running = False

for auto in autot:
    print(f"auton tunnus {auto.rekisteritunnus} , huippunopeus {auto.huippunopeus}, ja kuljettu matka {auto.kuljettumatka}")