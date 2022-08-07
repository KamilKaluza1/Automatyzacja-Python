cat_names = []

while True:
    name = input(f'Podaj imię kota numer {len(cat_names) +1}, ewentualnie nic nie wpisuj by zakończyć: ')
    if name == '':
        break
    cat_names = cat_names + [name]

print('Koty:')
for name in cat_names:
    print(name)