



velo = int ( input('Digite a velo do carro: '))
if (velo > 80):
    multa = (80 - velo) * 7
    print('''vc foi multado!! A milta custa R$7,00 por KM acima do limite. 
    O valor da multa é de R${:.2f}'''.format(abs(multa)))