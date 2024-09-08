



from random import randint
from time import sleep

num_pc = randint(0, 5)
num_user = int (input('Digite um Numero de 0 a 5: '))
print('PROCESANDO...')
sleep(2)
if (num_user <= 5):
    if (num_pc == num_user):
        print('Voce Ganhou!!!')
    else:
        print('Voce Perdeu :(')
else:
    print('Numero invalido!! Digite novamente.')
    num_user = int(input('Digite um Numero de 0 a 5: '))

