



salario = float (input('Digite seu salario: '))
if salario >= 1250.00:
    n_salario = (salario * 0.10 ) + salario
else:
    n_salario = (salario * 0.15) + salario
print('Seu novo salario sera de R${}'.format(n_salario))