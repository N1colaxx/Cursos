


def cal_pa (t, r):
    lista = []

    for i in range(10):
        res_pa = t + (i * r)
        lista.append(res_pa)
    return lista

def add_nu(novo_nu, t, r):
    lista = []
    l_nt = []

    novo_nu = int(novo_nu)
    loop = 10 + novo_nu

    for i in range(loop):
        res_pa = t + (i * r)
        lista.append(res_pa)

        if i >= 10:
            l_nt.append(res_pa)
    return lista, l_nt

print('Descobrindo os 10 primeiros numeros da PA! ')

while True:

    termo = int( input('informe o 1° termo da PA: '))
    razao = int( input('informe a razão da PA: '))

    pa = cal_pa(termo, razao)
    print('\n Os 10 primeiros termos são: \n {}'.format(pa))


    while True:
        print('\n Quer mostrar mais algum termo? S/N?')
        res = input(' Digite aqui: ').strip().upper()

        if res in ['S', 'N']:
            if res == 'S':
                novo_numero = input(' Mais quantos ? Digite aqui: ')
                nova_pa, novo_t = add_nu(novo_numero, termo, razao)

                print(' Os novos termos são: {}'.format(novo_t))
                print(' A nova PA é essa: {}'.format(nova_pa),)


                print('\n\nQuer mostrar mais algum termo? S/N?')
                res = input('\n Digite aqui: ').strip().upper()

            else:
                print('\n Ok, tchau \n ')
                break
        else:
            print('"ERRO" Opção invalida!!')
