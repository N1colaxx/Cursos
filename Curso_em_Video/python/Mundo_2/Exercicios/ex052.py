



num = float( input('Digite um N°: '))

if (num % 1 == 0) and (num % num == 0) and (num % 2 != 0):
    print(f'Este N° {num:.0f} é primo ')
else:
    print(f'Este N° {num:.0f} NÂO é primo')