class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat = []

    #metodi jonka parametrinä annetaan viittaus Koira olioon

    def koira_sisaan(self, koira):
        self.koirat.append(koira)
        print(f'{koira.nimi} lisättiin sisään hoitolaan {self.nimi}')
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f'{koira.nimi} lähti hoitolasta {self.nimi}')
        return

    def printtaakoirat(self):
        print(f'{self.nimi} on seuraavat koirat')
        for koira in self.koirat:
            print(koira.nimi)

    def tervehdikoiria(self, kerrat):
        print('tervehditään koiria ja jokainen haukkuu')
        for koira in self.koirat:
            koira.hauku(kerrat)

class Yritys:
    def __init__(self, nimi, osote):
        self.nimi = nimi
        self.osote = osote
        self.omistus = []
    def omistaa(self, hoitola):
        self.omistus.append(hoitola)
    def tulostahoitolat(self):
        for hoitola in self.omistus:
            print(hoitola.nimi)

    def anna_joululahja(self):
        print('Yritys antaa joululahjan jokaiselle koiralle')
        for hoitola in self.omistus:
            print(f'annetaan lahjoja {hoitola.nimi} koirille')
            for koira in hoitola.koirat:
                print(f'{koira.nimi} saa lahjaksi luun')
                koira.hauku(1)
#luodaan hoitolat
hoitola1 = Hoitola('onnentassu')
hoitola2 = Hoitola('pikkukoirat')
#luodaan koirat
koira1 = Koira("jaska",2010, "ajajajaj")
koira2 = Koira("jyri", 2012, "shadapa")
koira3 = Koira("jarkko", 2018, "jaaahaaa")
koira4 = Koira("jarmo", 2020, "WUFWUF")
koira1.hauku(1)
koira2.hauku(1)
koira3.hauku(1)
koira4.hauku(1)

#laitetaan koirat hoitolaan
hoitola1.koira_sisaan(koira1)
hoitola1.koira_sisaan(koira2)
hoitola2.koira_sisaan(koira3)
hoitola2.koira_sisaan(koira4)

hoitola1.printtaakoirat()
hoitola1.tervehdikoiria(1)

hoitola1.koira_ulos(koira1)
yritys1 = Yritys("musti","yea1" )
yritys1.omistaa(hoitola1)
yritys1.omistaa(hoitola2)
yritys1.tulostahoitolat()

yritys1.anna_joululahja()