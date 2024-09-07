



frase = input('Digite uma frase: ')

A = frase.count('a', )
P = frase.find('a', )
U = frase.rfind('a')

if U or P != -1:
    print('''
 A letra -> A aparece {} vez 
 Na posição {} por Primeiro
 Na posição {} por Ultimo
'''.format(A, P, U))
    print('\n-1 = não existe!!')
else:
    print('A palavra "Python" não foi encontrada.')