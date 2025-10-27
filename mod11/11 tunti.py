class Elain:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

    def tulosta_tiedot(self):
        print(f'{self.nimi}, syntymävuosi: {self.syntymävuosi}')


class Koira(Elain):
    def __init__(self, nimi, syntymävuosi, haukahdus="vuh vuf"):
        self.haukahdus = haukahdus
        super().__init__(nimi, syntymävuosi)
    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Kissa(Elain):
    def __init__(self, nimi, syntymävuosi):
        super().__init__(nimi, syntymävuosi)
koira = Koira("jarkko", 2020)
koira.hauku(2)
kissa = Kissa("jyri", 2022)
kissa.tulosta_tiedot()