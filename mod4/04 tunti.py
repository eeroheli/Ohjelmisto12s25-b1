#toistolause eli silmukka while

'''
suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print('totta')
    print('on vain kerran')

print('loppu')
'''

#iteraattori ja while
toistojen_lkm = 10
i = 0

while i < toistojen_lkm :
    i = i + 1
    #i += 1 nopeempi
    print(f'iteroiva silmuka, i:n arvo {i}')

print(f'i:n arvo lopuksi {i}')