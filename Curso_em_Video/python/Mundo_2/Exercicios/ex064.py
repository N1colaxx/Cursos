


print('Prog para somar numeros, para somente se digitar o numero: 999')


soma = 0
num_di = 0
while True:
    try:
        num = int(input('Digite um N° inteiro: '))
    except ValueError:
        print('"ERRO" Vc não digitou um n° INT!')
    else:
        if num == 999:
            print('=-=' * 15)
            print('Vc digitou o n°999 então estamos parando!')
            print('Vc digitou {} numeros, e a soma deles ficou: {} '.format(num_di, soma))
            break
        soma = soma + num
        num_di += 1





