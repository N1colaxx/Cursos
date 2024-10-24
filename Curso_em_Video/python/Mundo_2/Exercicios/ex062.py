

print('Descobrindo PA! ')

while True:
    lista = []

    n1 = int( input('informe o 1° termo da PA: '))
    r = int( input('informe a razão da PA: '))

    for i in range (10):
        pa =  n1 + (i * r)
        lista.append(pa)
    print('Os 10 primeiros termos da PA são: \n {}'.format(lista))


    while True:
        print('Quer mostrar mais algum termo? S/N?')
        res = input('Digite aqui: ').strip().upper()

        if res in ['S', 'N']:
            if res == 'S':
                res = 'Mais quantos ? Digite aqui: '
            else:
                print('\n Ok, tchau \n ')
                break
        else:
            print('"ERRO" Opção invalida!!')
