# 1. Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen,
# ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.
kuha = float(input('Anna kuhan pituus: '))
kuhan_pituus = 37 - kuha
if kuha >= 37:
    print('Kuha on sopivan mittainen!')
else :
    print(f'Kuha on {kuhan_pituus} cm liian lyhyt heitä veteen!')

#2. laivan hyttiluokka

hyttiluokka = input('Anna hyttiluokka: ')
if hyttiluokka == 'LUX' :
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == 'A' :
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'B' :
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'C' :
    print('C on ikkunaton hytti autokannen alapuolella.')
else :
    print('virheellinen hyttiluokka!')

#3. hemoglobiiniarvo

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input('Anna sukupuoli: ')
hemoglobiiniarvo = float(input('Anna hemoglobiiniarvo: '))
if sukupuoli == 'mies':
    if hemoglobiiniarvo < 134:
        print('Hemoglobiini arvosi ovat alhaiset.')
    elif hemoglobiiniarvo >= 134 and hemoglobiiniarvo <= 195:
        print('Hemoglobiini arvosi ovat normaalit.')
    elif hemoglobiiniarvo > 195:
        print('Hemoglobiini arvosi ovat korkeat.')
if sukupuoli == 'nainen':
    if hemoglobiiniarvo < 117:
        print('Hemoglobiini arvosi ovat alhaiset.')
    elif hemoglobiiniarvo >= 117 and hemoglobiiniarvo <= 175:
        print('Hemoglobiini arvosi ovat normaalit.')
    elif hemoglobiiniarvo > 175:
        print('Hemoglobiini arvosi ovat korkeat.')

#4. Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input('Anna vuosi: '))
if vuosi % 100 == 0 and vuosi % 400 == 0 :
    print('vuosi on karkausvuosi1')
elif vuosi % 4 == 0 and vuosi % 100 != 0 :
    print('vuosi on karkausvuosi2')
else:
    print('vuotesi ei ole karkausvuosi')