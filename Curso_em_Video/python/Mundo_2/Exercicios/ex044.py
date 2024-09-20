

vfp = float
for_pagamento= str

vp = float(input('\nQual o valor do produto: '))
print('''Opções de pagamento?
    1 = A vista, 10% desconto
    2 = A vista no cartão, 5% desconto 
    3 = Em ate 2x no cartão, preço normal
    4 = 3x ou mais no cartão, 20% juros
''')
for_paga = int(input('Qual a forma de pagamento: '))

if for_paga == 1:
    vfp = vp - (vp * (10/100))
    for_pagamento = 'A vista, 10% desconto'

elif for_paga == 2:
    vfp = vp - (vp * (5/100))
    for_pagamento = 'A vista no cartão, 5% desconto '

elif for_paga == 3:
    vfp = vp
    for_pagamento = 'Em ate 2x no cartão, preço normal'

elif for_paga == 4:
    vfp = vp + (vp * 20/100)
    for_pagamento = '3x ou mais no cartão, 20% juros'

else:
    vfp = 0
    for_pagamento = '\033[4;41m Opção invalida \033[m'

print(''' 
    Valor final do produto é: R${}
    Forma de pagamento é: {}
'''.format(vfp, for_pagamento))