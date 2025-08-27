#5.Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).
kokeilut = 0
app_running = True
ktunnus = 'python'
salasana = 'rules'
while kokeilut <= 5 and app_running:
    kokeilut += 1
    syötetty_ktunnus = input('anna käyttäjätunnus: ')
    syötetty_salasana = input('anna salasana: ')
    if syötetty_ktunnus == ktunnus:
        print('Tervetuloa!')
        app_running = False
    elif kokeilut == 5:
        print('Pääsy evätty')
