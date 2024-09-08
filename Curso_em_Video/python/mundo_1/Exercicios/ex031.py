



dv = int (input('Digite a distancia da viagem: '))

if dv <= 200:
    va_200k = dv * 0.50
    print('O valor da viagem é de R${:.2f}'.format(va_200k))
else:
    va = dv * 0.40
    print('O valor da viagem é de R${:.2f}'.format(va))