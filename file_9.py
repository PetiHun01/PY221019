f = int(input('Írd be az autód fogyasztását (L/100Km): '))
a = int(input('Írd be a benzin árát (Ft/L): '))
u = int(input('Írd be a megteendő út hosszát (Km): '))
print(f'Az útiköltség {u/f*a}Ft')