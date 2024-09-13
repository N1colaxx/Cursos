



from time import sleep

peso = float(input('\nInforme seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc >= 40:
    res = 'Obesidade mórbida'

elif imc >= 30:
    res =  'Obesidade'

elif imc >= 25:
    res = 'Sobrepeso'

elif imc >= 18.5:
    res = 'Peso Ideal'

else:
    res = 'Abaixo do Peso!'

print('Calculando...')
sleep(1)
print('Resultado: {}'.format(res))