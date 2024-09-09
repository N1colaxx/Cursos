



lista = []
for loop in range (1, 4):
    reta = float( input('Digite o valor da reta N°{}: '.format(loop)))
    lista.append(reta)
r1 = lista [0]
r2 = lista [1]
r3 = lista [2]
triangulo = (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1)
if triangulo == True:
    print('''
        Com esses tres valores vc pode obter uma reta.
        Valor 1= {}
        Valor 2= {}
        Valor 3= {}
    '''.format(r1, r2, r3))
else:
    print('''
        Com esses tres valores vc Não pode obter uma reta.
        Valor 1= {}
        Valor 2= {}
        Valor 3= {}
    '''.format(r1, r2, r3)) 