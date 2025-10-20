#3. Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
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

auto = Auto("ABC-123", 142)