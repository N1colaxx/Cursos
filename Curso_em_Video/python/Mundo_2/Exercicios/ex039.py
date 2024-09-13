



#from time import sleep
from datetime import datetime


ano_nas = int (input('Insira seu ano de nascimento: '))
print("PROCESSANDO...")

ano_atual = datetime.now().year

idade = ano_atual - ano_nas

if (idade <= 17):
    print('Vc ainda irá sealistar!')
    tf =  18 - idade
    print('Falta {} anos para seu alsitamento.'.format(tf))
elif (idade == 18):
    print('Vc esta na idade correta para o alsitamento!')
else:
    print('Ja passou da hora do seu alistamento!!')
    tp = idade - 18
    print('Já passou {} anos para seu alsitamnto.'.format(tp))

