# 1. Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
vuodenaika = ('talvi', 'talvi', 'kevät', 'kevät','kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy', 'syksy', 'talvi' )
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukausi = vuodenaika[järjestysnumero-1]
print (f"{järjestysnumero}. kuukauden vuodenaika on {kuukausi}.")
