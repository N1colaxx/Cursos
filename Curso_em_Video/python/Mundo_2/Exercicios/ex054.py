



from datetime import datetime

maior = 0
menor = 0
for i in range(1, 7+1):
    anos_nas = int( input('Digite seu ano de nascimento: '))

    ano_atual = datetime.now().year
    if ano_atual - anos_nas == 21:
        maior += 1
    else:
        menor += 1