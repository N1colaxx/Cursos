



from random import randint
from time import sleep

num_pc = randint(0, 5)
print('\nAcerte o N° q o PC ta processando. ')

while True:
    num_user = int (input('Digite um Numero de 0 a 5: '))
    print('PROCESANDO...')
    sleep(2)
    if num_user <= 5:
        if num_pc == num_user:
            print('Voce Ganhou!!! \n')
            print('Jogo Encerrado!')
            break
        else:
            print('Voce Perdeu :( \n')
            print('Jogo Encerrado!')
            break
    else:
        print('Numero invalido!! Digite novamente. \n')

