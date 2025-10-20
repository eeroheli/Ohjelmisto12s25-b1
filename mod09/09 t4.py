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
auto = []
for i in range(1, 11):
    auto.append(Auto(f"ABC-{i}", random.randint(100, 200)))

game_running = True
while game_running:
    t = 0
    for i in range(len(auto)):
        auto(t).kiihdyta(random.randint(-10, 15))
        auto(t).kulje(1)
        t = t + 1
    for i in auto:
        if auto[t].kuljettumatka >= 10000:
            game_running = False