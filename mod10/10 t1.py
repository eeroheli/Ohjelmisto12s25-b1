# 1. Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit
# ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.location = 0


    def up(self):
        self.location += 1
        print(f'olet nyt kerroksessa {self.location}')
        if self.location >= self.ylin:
            self.location = self.ylin

    def down(self):
        self.location -= 1
        print(f'olet nyt kerroksessa {self.location}')
        if self.location <= self.alin:
            self.location = self.alin

    def siirry(self,kerros):
        moving = True
        while moving:
            if self.location < kerros:
                self.up()
            elif self.location > kerros:
                self.down()
            elif self.location == kerros:
                moving = False
h1 = Hissi(-5, 5)
h1.siirry(3)
h1.siirry(-2)