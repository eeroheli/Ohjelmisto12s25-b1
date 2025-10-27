#2. Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
# jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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
        self.kuljettumatka += aika * self.nopeusnyt

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Bensaauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankinkoko = tankinkoko

sauto = Sähköauto("ABC-15", 180 , 52.5)
bauto = Bensaauto("ABC-123", 165, 32.3)
sauto.kiihdyta(145)
bauto.kiihdyta(125)
sauto.kulje(3)
bauto.kulje(3)
print(f"auton tunnus {sauto.rekisteritunnus} , huippunopeus {sauto.huippunopeus}, ja kuljettu matka {sauto.kuljettumatka}km")
print(f"auton tunnus {bauto.rekisteritunnus} , huippunopeus {bauto.huippunopeus}, ja kuljettu matka {bauto.kuljettumatka}km")