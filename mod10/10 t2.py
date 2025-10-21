# 2. Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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

class Talo:
    def __init__(self, alin, ylin, kpl):
        self.alin = alin
        self.ylin = ylin
        self.kpl = kpl
        self.hissit = []
        for i in range(kpl):
            self.hissit.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, nro, kerros):
        self.hissit[nro].siirry(kerros)

talo1 = Talo(0, 5, 2)
talo1.aja_hissia(0, 2)