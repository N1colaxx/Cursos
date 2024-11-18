
from random import randint
from time import sleep

num_pc = randint(0, 5)
print('\nAcerte o N° q o PC ta processando. ')

palptes = 0
while True:
    num_user = int (input('Digite um Numero de 0 a 5: '))
    palptes += 1
    print('PROCESANDO...')
    sleep(2)
    if num_user <= 5:
        if num_pc == num_user:
            print(f'Voce Ganhou!!! com {palptes} paltipes\n')
            print('Jogo Encerrado!')
            break
        else:
            print('Voce Perdeu :( \n')
            print('Jogo Encerrado!')
            break
    else:
        print('Numero invalido!! Digite novamente. \n')

