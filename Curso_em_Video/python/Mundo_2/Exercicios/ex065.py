lista = []
soma = 0
digitou = 0

while True:
    try:
        num = int( input('\n Digite um N° int: '))
    except ValueError:
        print('"ERRO" Numero digitado não é INT')
    else:
        soma += num
        digitou += 1
        lista.append(num)

    while True:
        res = input('\n Quer continuar S/N? ').strip().upper()
        if res == 'S':
            break

        elif res == 'N':
            media = soma / digitou
            maior = max(lista)
            menor = min(lista)

            print('''
            vc digitou {} vezes.
            A soma dos n° ficou : {}
            A media = {}
            O Maior N° é: {}
            O Menor N° é: {}
            '''. format(digitou, soma, media, maior, menor))
            exit()

        else:
            print('Erro: Opção invalida!! Digite nova mente.')

