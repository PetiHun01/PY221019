from unicodedata import name


vez1 = input('Első Vezetéknév: ')
vez2 = input('Második Vezetéknév: ')
ker1 = input('Első Keresztnév: ')
ker2 = input('Második Keresztnév: ')
nevek = (f'{vez1+ker1}, {vez1+ker2}, {vez2+ker1}, {vez2+ker2}')
print(f'Lehetséges nevek: {nevek}')