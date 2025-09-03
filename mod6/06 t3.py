#3. Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def litralaskuri():
    gallons = float(input('Gallonamäärä: '))
    litrat = gallons * 3.785
    if gallons < 0:
        print('annoit negatiivisen arvon')
    else:
        print(f'{gallons} galloonaa on litroina {litrat}')
    return litrat

litrat = 1
while litrat > 0:
    litralaskuri()
    litrat = litralaskuri()