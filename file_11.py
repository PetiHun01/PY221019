alma = int('345')
szilva = int('220')
szolo = int('375')
print(f'Szőlő Ára: {szolo} FT/KG\n A Szilva ára {szilva}FT/KG\n Az Alma ára {alma}FT/KG')
vas = (input.split('Mennyit  szeretnél vásárolni és miből?'))
if vas == ('Szőlő'):
    print(f'Fizetendő:{vas*szolo}')