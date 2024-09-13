



# Jogo do Joquempô

from random import randint

# Inicialização das VAR

# var Quem ganhou
resultado = ''
cont_vt_user = int(0)
cont_empate = int(0)
cont_vt_pc = int(0)


#var do loop
jg_novo = 'S'

while jg_novo.upper() == 'S':

    print('-=-'*10)
    print('Jogo do Joquempô'.center(30))
    print('-=-'*10)

    print('''       Pedra = 1
       Papel = 2
       Tesoura = 3 ''')
    print('-=-'*10)


    #Caso digite algo q n seja um Numero exibe a msg de erro
    try:
        es_user = int(input('Qual sua jogada: '))
    except ValueError:
        print('\033[4;40;41m Entrada inválida \033[m')
        continue  # Volta ao início do loop se a entrada não for um número

    # Valida a jg do User
    if es_user == 1:
        jg_user = 1 # 1 = pedra
        print('User escolheu 1 = pedra')
    elif es_user == 2:
        jg_user = 2 # 2 = papel
        print('User escolheu 2 = papel')
    elif es_user == 3:
        jg_user = 3 # 3 = tesoura
        print('User escolheu 3 = tesoura')
    else:
        print('\033[4;40;41m Jogada INVALIDA \033[m')
        continue # Volta ao início se a jogada for diferente de 1, 2 ou  3

    #faz a Jg PC
    jg_pc = randint(1,3)
    if jg_pc == 1:
        jg_pc = 1
        print('PC escolheu 1 = pedra')
    elif jg_pc == 2:
        jg_pc = 2
        print('PC escolheu 2 = papel')
    elif jg_pc == 3:
        jg_pc = 3
        print('Pc escolheu 3 = tesoura')


    # Ver quem ganhou
    # 1 = Pedra, 2 = Papel, 3 = tesoura
    if (jg_user == 1) and (jg_pc == 3) or (jg_user == 2) and (jg_pc == 1) or (jg_user == 3) and (jg_pc == 2):
        resultado = 'Vc ganhou!'
        cont_vt_user  += 1
    elif jg_user == jg_pc:
        resultado = 'Empatou!'
        cont_empate += 1
    else:
        resultado = 'Pc venceu!'
        cont_vt_pc += 1

    print('\nResultado: {}'.format(resultado))
    print('-=-'*10)


    jg_novo = str(input('Quer jogar novamente? S/N? '.strip()))
    jg_novo = jg_novo.upper()


print('\nVc escolher para muito obr.')
print(''' 
Quantidade de vitorias do User é: {}
Quantidade de Vitorias do Pc é: {}
Qauntidade de Empates é: {}
'''.format(cont_vt_user, cont_empate, cont_vt_pc))

