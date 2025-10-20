#2. Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

app_running = True
while app_running:
    tuuma = float(input('anna tuumamäärä'))

    if tuuma >= 0:
        sentit = tuuma * 2.54
        print(f'Tuumat ovat senttimetreinä {sentit} ')
    else :
        app_running = False
