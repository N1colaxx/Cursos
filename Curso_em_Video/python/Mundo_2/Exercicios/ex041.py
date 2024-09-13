

from time import sleep

ano_nas = int(input('Informe seu ano de nascimento: '))
print('Carregando...')
sleep(1)

cat = str
if ano_nas <= 9:
    cat = 'Mirim'

elif ano_nas <= 14:
    cat = 'Infantil'

elif ano_nas <= 19:
    cat = 'Junior'

elif ano_nas <= 20:
    cat = 'Sênior'
else:
    cat = 'Master'
print('Sua categoria é {}'.format(cat))
