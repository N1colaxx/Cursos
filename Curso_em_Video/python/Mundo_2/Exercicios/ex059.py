

while True:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))

    print('\n Agora faça sua escolha: ')
    print(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do progama ')

    escolha = input('\n Digite aqui: ').strip()

    if escolha == '1':
        soma = n1 + n2
        res = soma

    elif escolha == '2':
        multiplicar = n1 * n2
        res = multiplicar

    elif escolha == '3':
        maior = max (n1, n2)
        res =  maior

    elif escolha == '4':
        print('Ok, digite onovos números. \n\n')
        continue

    elif escolha == '5':
        print('Ok, obg tchau! ')
        break

    else:
        print('"ERRO" Opção invalida!! Digite novamente. \n\n')

    if escolha in ['1', '2', '3',]:
        print('\n',f'Vc escolehu o N°{escolha} resultado ==>', res)
