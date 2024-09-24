

maior = 0

lista_peso = []

for i in range(1, 5+1):
    peso = float( input('Digite seu peso: '))
    lista_peso.append(peso)

    if peso > maior:
        maior = peso

# menor = lista_peso[0] # faz menor iniciar com o 1° valor da lista
# for peso in lista_peso:
#     if peso < menor:
#         menor = peso
#
menor = min(lista_peso)

print('''
      maior peso {}
      menor peso {}
'''.format(maior, menor))

